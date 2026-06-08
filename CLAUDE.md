# Project Reference — Teserrufat (Ztbagro)

Django site for an agriculture company ("Teserrufat"). Multi-language (az/ru) via `django-modeltranslation`.

## Project Structure
- `core/` — Django project settings, root URLs, WSGI/ASGI
- `teserrufat/` — main app: models, admin, views, urls, translation, context processors
- `services/` — shared helpers used across the app:
  - `choices.py` — shared choice tuples (e.g. `PAGE_CHOICES` for `TitleDescription.page_type`)
  - `uploader.py` — `Uploader` static methods defining `upload_to` paths per model
  - `generator.py` — `Generator.create_slug_shortcode()` used in model `save()` overrides for slug generation
  - `mixin.py` — abstract base models `DateMixin` (created_at/updated_at) and `SlugMixin` (slug field)
  - `extract.py` — misc extraction helpers
- `templates/` — Django templates; most extend `base.html` via `{% extends 'base.html' %}{% block title %}...{% block body %}`. **Exception: `index.html` is standalone and does not extend `base.html`** — it duplicates the full header/nav/footer, so any navbar/footer change must be applied in both places.
- `static/` — static assets (CSS/JS/images); `static/assets/js/script.js` is the main JS file, wrapped in `(function($) { ... })(window.jQuery);`, with numbered sections inside `$(document).ready(...)` and `$(window).on('load', ...)`.
- `media/` — user-uploaded content (gitignored)
- `locale/` — translation catalogs

## App Conventions
- **Models**: inherit `DateMixin`/`SlugMixin` from `services/mixin.py`; define `__str__`, `Meta` with Azerbaijani `verbose_name` strings and `ordering = ("-created_at",)`; override `save()` to generate slugs via `Generator.create_slug_shortcode()`.
- **Uploads**: define `upload_to` as a static method on `Uploader` (`services/uploader.py`), not inline lambdas — keeps upload paths centralized and discoverable.
- **Translatable models**: register in `teserrufat/translation.py` using `TranslationOptions`; long-form content fields use `RichTextField` (django-ckeditor).
- **Admin**: register translatable models with `TranslationAdmin`; use `TranslationTabularInline`/`StackedInline` for related inlines. Django admin doesn't support nested inlines — models that need their own inline (e.g. a table-of-rows under a table under a product) are registered as separate top-level admin entries.
- **Views**: list views follow the `services_view` pagination pattern — `Paginator` with `PageNotAnInteger`/`EmptyPage` handling, optional `?cat=` category filter, `page_type`-scoped `TitleDescription` lookups for SEO meta/banner per page.
- **Choices**: page types for `TitleDescription` (per-page SEO title/description/banner image) live in `PAGE_CHOICES` in `services/choices.py` — add new entries there when introducing a new page.
- **Global context**: `teserrufat.context_processors.my_sender` injects shared template context (`categories`, `product_categories`, `index_config`, `titles`, `social_media`) available on every page.
- **i18n**: use `{% trans '...' %}` — must stay on a **single line**; multi-line `{% trans %}` tags render as literal text (Django's `tag_re` lacks `re.DOTALL`).
- **JS**: add new behavior as a numbered section inside the existing `$(document).ready(...)` / `$(window).on('load', ...)` blocks in `static/assets/js/script.js`, following the existing numbering convention.
