"""Fill lecture as-of markers from mkdocs.yml extra.reference_date.

{{ reference_date }} becomes the ISO date (2026-10-18).
{{ reference_date_ko }} becomes the spoken form (2026년 10월 18일).
"""


def on_page_markdown(markdown, /, *, page, config, files):
    iso = config.extra["reference_date"]
    year, month, day = iso.split("-")
    spoken = f"{year}년 {int(month)}월 {int(day)}일"
    return markdown.replace("{{ reference_date_ko }}", spoken).replace(
        "{{ reference_date }}", iso
    )
