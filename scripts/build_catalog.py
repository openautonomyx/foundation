#!/usr/bin/env python3
"""Validate the registry and build a searchable catalog.

Outputs:
  - registry/INDEX.md       (human-readable index)
  - docs/catalog.json       (machine-readable, powers the search UI)
  - docs/index.html         (static client-side searchable catalog)

Exits non-zero on schema-validation errors or dangling relationship edges,
so it doubles as the CI gate.
"""
import glob, json, os, sys, warnings
warnings.filterwarnings("ignore")
import yaml
from jsonschema import Draft202012Validator, RefResolver

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

DIR_TO_SCHEMA = {
    "capabilities": "capability", "controls": "control", "risks": "risk",
    "agents": "agent", "identities": "identity", "workspaces": "workspace",
    "decisions": "decision", "standards": "standard", "protocols": "protocol",
    "skills": "skill", "knowledge": "knowledge-asset", "twins": "digital-twin",
    "taxonomies": "taxonomy", "entities": "entity",
}
TITLE = {
    "capabilities": "Capabilities", "controls": "Controls", "risks": "Risks",
    "agents": "Agents", "identities": "Identities", "workspaces": "Workspaces",
    "decisions": "Decisions", "standards": "Standards", "protocols": "Protocols",
    "skills": "Skills", "knowledge": "Knowledge Assets", "twins": "Digital Twins",
    "taxonomies": "Taxonomies", "entities": "Entities",
}
ORDER = ["entities", "capabilities", "agents", "identities", "workspaces", "decisions",
         "risks", "controls", "protocols", "skills", "standards", "knowledge",
         "twins", "taxonomies"]

# Category assignment. Non-standard objects map by directory; standards map
# by their standardType domain.
DIR_CATEGORY = {
    "entities": "Governance",
    "capabilities": "Governance", "risks": "Governance", "controls": "Governance",
    "decisions": "Governance", "agents": "Agent", "identities": "Identity & Access",
    "workspaces": "Agent", "skills": "Agent", "protocols": "Interoperability",
    "twins": "Agent", "knowledge": "Knowledge", "taxonomies": "Taxonomy",
}
STD_CATEGORY = {
    "identity": "Identity & Access", "authentication": "Identity & Access",
    "authorization": "Identity & Access", "policy": "Governance & Policy",
    "observability": "Observability", "orchestration": "Orchestration & Runtime",
    "data": "Data & Models", "interoperability": "Interoperability",
    "packaging": "Packaging & Supply Chain", "transport": "Networking",
    "agent": "Agent Ecosystem",
}


def categorize(obj, d):
    if d == "standards":
        return STD_CATEGORY.get(obj.get("standardType", ""), "Standard")
    return DIR_CATEGORY.get(d, "Other")


def tags_for(obj, d, stype):
    tags = []
    tags.extend(obj.get("mappedConcepts", []) or [])
    if obj.get("standardType"):
        tags.append(obj["standardType"])
    if obj.get("skillType"):
        tags.append(obj["skillType"])
    if obj.get("adoptionPosture"):
        tags.append(obj["adoptionPosture"])
    mat = obj.get("upstreamMaturity", "")
    for kw in ("cncf-graduated", "cncf-incubating", "cncf-sandbox", "openid-final",
               "linux-foundation", "ietf-internet-draft", "placeholder"):
        if kw in mat:
            tags.append(kw)
    org = obj.get("organization", "")
    if "CNCF" in org:
        tags.append("cncf")
    if "AGenNext" in org:
        tags.append("agennext")
    # Wikipedia / external source topic as a tag
    src = str(obj.get("source", "")) + " " + str(obj.get("specReference", ""))
    if "wikipedia.org/wiki/" in src:
        tags.append("wikipedia")
        try:
            topic = src.split("wikipedia.org/wiki/")[1].split()[0].split("#")[0]
            topic = topic.replace("_", " ").replace("%E2%80%93", "-").strip()
            if topic and topic.lower() != "main page":
                tags.append(topic)
        except Exception:
            pass
    if "arxiv.org" in src or "arXiv" in str(obj.get("source", "")):
        tags.append("arxiv")
    # de-dupe, keep order
    seen, out = set(), []
    for t in tags:
        t = str(t).strip()
        if t and t.lower() not in seen:
            seen.add(t.lower()); out.append(t)
    return out


def load_schemas():
    store = {}
    for sf in glob.glob("schemas/*.json"):
        store[os.path.basename(sf)] = json.load(open(sf))
    return store


def main():
    store = load_schemas()
    nodes, defined, refs, errors = [], set(), set(), []
    for d in ORDER:
        stype = DIR_TO_SCHEMA[d]
        schema = store[f"{stype}.schema.json"]
        resolver = RefResolver(base_uri="", referrer=schema, store=store)
        validator = Draft202012Validator(schema, resolver=resolver)
        for f in sorted(glob.glob(f"registry/{d}/*.yaml")):
            obj = yaml.safe_load(open(f))
            if not obj:
                continue
            defined.add(obj["id"])
            rels = obj.get("relationships") or []
            for r in rels:
                if isinstance(r, dict) and "target" in r:
                    refs.add(r["target"])
            for e in validator.iter_errors(obj):
                errors.append(f"{f}: {e.message}")
            nodes.append({
                "id": obj["id"], "dir": d, "type": stype,
                "category": categorize(obj, d),
                "tags": tags_for(obj, d, stype),
                "name": obj.get("name", ""), "description": obj.get("description", ""),
                "status": obj.get("status") or obj.get("lifecycleState", ""),
                "standardType": obj.get("standardType", ""),
                "adoptionPosture": obj.get("adoptionPosture", ""),
                "organization": obj.get("organization", ""),
                "specReference": obj.get("specReference", ""),
                "relationships": [{"type": r.get("type"), "target": r.get("target")}
                                  for r in rels if isinstance(r, dict)],
            })
    dangling = sorted(refs - defined)

    ok = not errors and not dangling
    # ---- catalog.json ----
    os.makedirs("docs", exist_ok=True)
    catalog = {"generated": "auto", "total": len(nodes),
               "counts": {d: sum(1 for n in nodes if n["dir"] == d) for d in ORDER},
               "valid": ok, "nodes": sorted(nodes, key=lambda n: (n["dir"], n["id"]))}
    json.dump(catalog, open("docs/catalog.json", "w"), indent=1)

    # ---- INDEX.md ----
    out = ["# Foundation Registry Index", "",
           "Auto-generated by `scripts/build_catalog.py`. Do not edit by hand.", "",
           f"**Total: {len(nodes)} governed nodes** — searchable catalog: `docs/index.html`", "",
           "| Type | Count |", "|---|---|"]
    for d in ORDER:
        out.append(f"| {TITLE[d]} | {catalog['counts'][d]} |")
    out.append("")
    for d in ORDER:
        items = [n for n in nodes if n["dir"] == d]
        if not items:
            continue
        out.append(f"## {TITLE[d]} ({len(items)})\n")
        if d == "standards":
            by = {}
            for n in items:
                by.setdefault(n["standardType"] or "other", []).append(n)
            for st in sorted(by):
                out.append(f"### {st} ({len(by[st])})\n")
                for n in sorted(by[st], key=lambda x: x["id"]):
                    out.append(f"- `{n['id']}` — {n['name']} ({n['adoptionPosture']})")
                out.append("")
        else:
            for n in sorted(items, key=lambda x: x["id"]):
                out.append(f"- `{n['id']}` — {n['name']}")
            out.append("")
    open("registry/INDEX.md", "w").write("\n".join(out))

    # ---- docs/catalog.html (search UI; index.html is the hand-authored home page) ----
    open("docs/catalog.html", "w").write(HTML)

    print(f"catalog: {len(nodes)} nodes | valid={ok} | dangling={dangling if dangling else 'NONE'}")
    if errors:
        print("SCHEMA ERRORS:")
        for e in errors[:50]:
            print(" ", e)
    if not ok:
        sys.exit(1)


HTML = r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>OpenAutonomyX — Registry Catalog</title>
<style>
  :root { color-scheme: light dark; }
  body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 0 auto; padding: 0 1rem 3rem; max-width: 1000px; }
  nav { font-size: .85rem; padding: .8rem 0; opacity: .8; }
  h1 { margin: .25rem 0; font-size: 1.4rem; }
  .sub { opacity: .7; font-size: .85rem; margin-bottom: 1rem; }
  .controls { position: sticky; top: 0; background: Canvas; padding: .75rem 0; display: flex; gap: .5rem; flex-wrap: wrap; border-bottom: 1px solid #8884; z-index: 5; }
  input, select { padding: .5rem .6rem; font-size: 1rem; border: 1px solid #8886; border-radius: 8px; background: Canvas; color: CanvasText; }
  #q { flex: 1; min-width: 200px; }
  #stats { font-size: .8rem; opacity: .7; margin: .6rem 0; }
  #active { font-size: .78rem; margin: .3rem 0; }
  .card { border: 1px solid #8884; border-radius: 10px; padding: .6rem .8rem; margin: .5rem 0; }
  .card h3 { margin: 0 0 .2rem; font-size: .98rem; }
  .id { font-family: ui-monospace, monospace; font-size: .8rem; opacity: .75; }
  .cat { font-size: .7rem; padding: .12rem .5rem; border-radius: 999px; background: #6691; border: 1px solid #66f6; }
  .badges { margin: .35rem 0 0; display: flex; gap: .35rem; flex-wrap: wrap; }
  .b { font-size: .68rem; padding: .12rem .45rem; border-radius: 999px; border: 1px solid #8886; opacity: .85; }
  .tag { cursor: pointer; }
  .tag:hover { background: #8882; }
  .desc { font-size: .86rem; margin: .35rem 0 0; opacity: .9; }
  a { color: inherit; }
</style>
</head>
<body>
<nav><a href="./index.html">&larr; OpenAutonomyX</a></nav>
<h1>Registry Catalog</h1>
<div class="sub" id="meta">loading…</div>
<div class="controls">
  <input id="q" type="search" placeholder="Search id, name, description, tags, organization…" autofocus>
  <select id="category"><option value="">All categories</option></select>
  <select id="type"><option value="">All types</option></select>
  <select id="domain"><option value="">All standard domains</option></select>
</div>
<div id="active"></div>
<div id="stats"></div>
<div id="list"></div>
<script>
let DATA = [], tagFilter = "";
const q=document.getElementById('q'), catSel=document.getElementById('category'),
      typeSel=document.getElementById('type'), domSel=document.getElementById('domain'),
      list=document.getElementById('list'), stats=document.getElementById('stats'),
      meta=document.getElementById('meta'), active=document.getElementById('active');
function esc(s){return (s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));}
function setTag(t){ tagFilter=t; render(); }
window.setTag=setTag;
function render(){
  const term=q.value.trim().toLowerCase(), cat=catSel.value, t=typeSel.value, dom=domSel.value;
  active.innerHTML = tagFilter ? 'tag: <span class="b">'+esc(tagFilter)+'</span> <a href="#" onclick="setTag(\'\');return false">clear</a>' : '';
  const out=DATA.filter(n=>{
    if(cat && n.category!==cat) return false;
    if(t && n.type!==t) return false;
    if(dom && n.standardType!==dom) return false;
    if(tagFilter && !(n.tags||[]).map(x=>x.toLowerCase()).includes(tagFilter.toLowerCase())) return false;
    if(!term) return true;
    return (n.id+' '+n.name+' '+n.description+' '+n.organization+' '+n.standardType+' '+(n.tags||[]).join(' ')).toLowerCase().includes(term);
  });
  stats.textContent = out.length+' of '+DATA.length+' nodes';
  list.innerHTML = out.slice(0,600).map(n=>{
    const badges=[n.type,n.standardType,n.adoptionPosture,n.status].filter(Boolean)
      .map(b=>'<span class="b">'+esc(b)+'</span>').join('');
    const tags=(n.tags||[]).slice(0,12).map(tg=>'<span class="b tag" onclick="setTag('+JSON.stringify(tg).replace(/"/g,'&quot;')+')">#'+esc(tg)+'</span>').join('');
    const link=n.specReference?' · <a href="'+esc(n.specReference)+'" target="_blank" rel="noopener">ref</a>':'';
    return '<div class="card"><h3>'+esc(n.name||n.id)+' <span class="cat">'+esc(n.category)+'</span></h3>'+
      '<div class="id">'+esc(n.id)+link+'</div>'+
      (n.description?'<div class="desc">'+esc(n.description)+'</div>':'')+
      '<div class="badges">'+badges+tags+'</div></div>';
  }).join('') + (out.length>600?'<p class="sub">Showing first 600. Refine your search.</p>':'');
}
fetch('./catalog.json').then(r=>r.json()).then(c=>{
  DATA=c.nodes;
  meta.textContent=c.total+' governed nodes · graph valid: '+c.valid;
  [...new Set(DATA.map(n=>n.category).filter(Boolean))].sort().forEach(x=>catSel.add(new Option(x,x)));
  [...new Set(DATA.map(n=>n.type))].sort().forEach(x=>typeSel.add(new Option(x,x)));
  [...new Set(DATA.map(n=>n.standardType).filter(Boolean))].sort().forEach(x=>domSel.add(new Option(x,x)));
  render();
});
[q,catSel,typeSel,domSel].forEach(el=>el.addEventListener('input',render));
</script>
</body>
</html>
"""

if __name__ == "__main__":
    main()
