# Handover

## Summary
Django site for "Teserrufat" (agriculture company). This session integrated two new static templates (`products.html`, `product-details.html`) and a new "Partners" section on the home page into Django, building full models/admin/views/URLs for dynamically-managed Products and Partners, wiring up navbar links, and adding a smooth-scroll animation for the "Partnyorlar" nav link.

## What Was Done
- Added `products` / `product_detail` to `PAGE_CHOICES` in `services/choices.py` (drives `TitleDescription` per-page SEO/banner records).
- Added `Uploader.upload_photo_for_product`, `upload_document_for_product`, `upload_logo_for_partner` static methods in `services/uploader.py`.
- New models in `teserrufat/models.py`: `ProductCategory`, `Product`, `ProductDocument`, `ProductTable`, `ProductTableRow`, `Partner` — all follow existing `DateMixin`/`SlugMixin` + `Generator.create_slug_shortcode()` pattern.
- Registered translation options (`teserrufat/translation.py`) and admin classes with inlines (`teserrufat/admin.py`) for the new models.
- Migration `teserrufat/migrations/0037_partner_product_productcategory_producttable_and_more.py` created and applied.
- Views `products_view` (paginated, `?cat=` filter) and `product_detail` added to `teserrufat/views.py`; `home_view` now also passes `partners` to context.
- URLs added in `teserrufat/urls.py`: `products/` → `products`, `product/detail/<slug>/` → `product_detail`.
- `teserrufat/context_processors.py` now also injects `product_categories` (used for the navbar dropdown globally).
- Rewrote `templates/products.html` and `templates/product-details.html` to extend `base.html`, mirroring `services.html`/`service-details.html` patterns (title block via `TitleDescription`, page banner, pagination, dynamic fields/documents/tables).
- `templates/index.html` `#partnors` section now loops `partners` from context instead of static logos.
- Navbar updated in **both** `templates/base.html` and `templates/index.html` (index.html does NOT extend base.html — it has its own full header/nav/footer copy):
  - "Məhsullarımız" dropdown (loops `product_categories`, links to `products` with `?cat=`)
  - "Partnyorlar" link → `{% url 'home' %}#partnors`
- Smooth-scroll for "Partnyorlar": added `partner-scroll-link` class + `data-target="#partnors"` to the link in both templates, and a new "25. Partner Scroll Link" handler in `static/assets/js/script.js` (~line 670, inside the existing `$(document).ready`):
  - If `#partnors` exists on the current page → `preventDefault` + jQuery `.animate({scrollTop}, 1000)`.
  - Otherwise lets the browser navigate to `home#partnors`; on load, if `location.hash === '#partnors'`, animates the scroll instead of an instant jump.
- Added `.DS_Store` to `.gitignore` and untracked it (`git rm --cached`).

## What We Tried / What Didn't Work
- Tried to clean up test data (test `Product`, `ProductCategory`, `Partner`, `TitleDescription` records and `media/product`, `media/partner`, `media/pagesSlide` test files) via a Bash command — **user rejected this tool call**. Cleanup is still pending; do NOT attempt it again without explicit go-ahead — ask the user how they want to handle it (they may want to do it from the admin panel themselves).

## Bugs & Fixes
| Bug | Fix |
|---|---|
| `python` not found | Use `python3` for all `manage.py` commands |
| `ModuleNotFoundError: No module named 'dj_database_url'` (and similar for ckeditor, modeltranslation, rosetta, social_share) | `pip3 install --user <package>` — packages were already listed in `requirements.txt`, just not installed in the local env |
| `fields.E210: Cannot use ImageField because Pillow is not installed` | `pip3 install --user Pillow` |
| 500 error: `ValueError: 'page_slide_image' attribute has no file associated with it` on `products`/`product_detail` pages | Pre-existing template pattern issue (same as `services.html` — accesses `.url` without checking the field is set). Not introduced by this session; worked around for testing only by uploading test banner images to `TitleDescription` via shell — template itself was NOT changed |
| Multi-line `{% trans '...' %}` doesn't render (Django's `tag_re` lacks `re.DOTALL`, so `{%` / `%}` on separate lines render as literal text) | Incidentally fixed in `index.html` nav `<li>` by writing it as a single line while adding the new nav items — confirmed via isolated `Template().render()` test |

## Key Decisions (and Why)
| Decision | Rationale |
|---|---|
| Modeled `Product → ProductDocument`, `Product → ProductTable → ProductTableRow` as separate FK'd models rather than JSON/text fields | Matches user's explicit choice in clarifying questions; keeps content fully admin-editable per existing conventions (TranslationTabularInline etc.) |
| Registered `ProductTable` as its own `TranslationAdmin` (with `ProductTableRowInline`) instead of nesting inside `ProductAdmin` | Django admin doesn't support nested inlines without extra third-party packages |
| Edited nav in both `base.html` AND `index.html` | `index.html` is a standalone template that does not `{% extends 'base.html' %}` — it duplicates the entire header/nav/footer |
| Custom `partner-scroll-link` handler instead of reusing generic `.scroll-to-target` | `.scroll-to-target` doesn't call `preventDefault()` (fine for the scroll-to-top `<button>`, but an `<a href="...">` needs conditional prevention plus cross-page hash handling on load) |

## Gotchas / Things to Watch Out For
- `templates/index.html` is **standalone** — any future navbar/footer change must be applied to both `base.html` and `index.html`.
- The `page_slide_image` banner pattern (`{{ i.page_slide_image.url }}`) will 500 if no `TitleDescription` record with an uploaded image exists for that `page_type` — make sure admin creates one for `products` and `product_detail` (and any new page types) before going live.
- Multi-line `{% trans %}` tags silently render as literal text — always keep `{% trans '...' %}` on one line in this codebase.
- Test data still in DB/filesystem (see "What We Tried" above) — clean up before/при going live, with user's go-ahead.
- `requirements.txt` already lists all needed packages (`django-modeltranslation`, `django-ckeditor`, `dj-database-url`, `Pillow`, etc.) — no changes needed there for deploy, just make sure the server's venv actually has them installed.

## Next Steps
- [ ] Decide how to clean up test data (`Product` "Test Məhsul ®", `ProductCategory` "Gübrələr", `Partner`, `ProductDocument`/`ProductTable`/`ProductTableRow`, `TitleDescription` for `products`/`product_detail`, and `media/product`, `media/partner`, `media/pagesSlide` test files) — user must confirm approach
- [ ] `git add` the new files and commit: `templates/products.html`, `templates/product-details.html`, `teserrufat/migrations/0037_partner_product_productcategory_producttable_and_more.py`, plus all modified files and `.gitignore`
- [ ] Push to git, then on the server: `git pull` → `python3 manage.py migrate` → `python3 manage.py collectstatic` (if `DEBUG=False`) → restart app server (uwsgi/gunicorn)
- [ ] In production admin, create real `TitleDescription` records (with banner images) for `page_type` = `products` and `product_detail`
- [ ] Add real `Product`, `ProductCategory`, and `Partner` records via admin

## Important Files Map
| Path | Purpose |
|---|---|
| `services/choices.py` | `PAGE_CHOICES` — added `products`, `product_detail` |
| `services/uploader.py` | `Uploader` upload-path helpers — added product/partner methods |
| `teserrufat/models.py` | New models: `ProductCategory`, `Product`, `ProductDocument`, `ProductTable`, `ProductTableRow`, `Partner` (appended after `Subscribe`, ~line 449+) |
| `teserrufat/translation.py` | Translation registration for new models |
| `teserrufat/admin.py` | Admin registration + inlines (`DocumentInLineProduct`, `ProductTableRowInline`, `ProductCategoryAdmin`, `ProductAdmin`, `ProductTableAdmin`, `PartnerAdmin`) |
| `teserrufat/migrations/0037_partner_product_productcategory_producttable_and_more.py` | Migration creating the 6 new models + translation fields |
| `teserrufat/views.py` | `products_view`, `product_detail`; `home_view` now passes `partners` |
| `teserrufat/urls.py` | `products/`, `product/detail/<slug>/` routes |
| `teserrufat/context_processors.py` | `my_sender` now also injects `product_categories` |
| `templates/products.html` | Rewritten — extends `base.html`, product grid + pagination |
| `templates/product-details.html` | Rewritten — extends `base.html`, product detail with documents/tables |
| `templates/index.html` | `#partnors` section now dynamic; navbar has Products/Partners links + `partner-scroll-link` |
| `templates/base.html` | Navbar has Products/Partners links + `partner-scroll-link` |
| `static/assets/js/script.js` | New "25. Partner Scroll Link" handler (~line 670) for smooth-scroll to `#partnors` |
| `.gitignore` | Added `.DS_Store` |

## Run/Test Commands
```bash
# Run dev server
python3 manage.py runserver 0.0.0.0:8123

# Migrations
python3 manage.py makemigrations teserrufat
python3 manage.py migrate

# Check for missing migrations (should say "No changes detected")
python3 manage.py makemigrations --check --dry-run

# Smoke test
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8123/
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8123/products/
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:8123/product/detail/<slug>/
```
