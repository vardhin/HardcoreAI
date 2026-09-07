"""
Patch built frontend bundle to remove Blue Pill default fallbacks.
Run from workspace root: python backend/scripts/patch_dist_remove_bluepill.py
This is a temporary hotfix. Rebuild frontend to make permanent.
"""
from pathlib import Path
p = Path("e:/PROGRAMMES/hardcoreai/frontend/dist/assets/index--mYAg-uj.js")
if not p.exists():
    print("dist file not found:", p)
    raise SystemExit(1)
s = p.read_text(encoding='utf-8')
orig = s
s = s.replace('"bluepill_f103c8"', '""')
s = s.replace("'bluepill_f103c8'", "''")
s = s.replace('||"""', '||""')
# Common patterns where fallback used with ||
s = s.replace('||""', '||""')
# Also replace occurrences where it's used as default without quotes
s = s.replace('bluepill_f103c8', '')
# Write backup
backup = p.with_suffix('.js.bak')
backup.write_text(orig, encoding='utf-8')
p.write_text(s, encoding='utf-8')
print('Patched', p, 'backup saved to', backup)
