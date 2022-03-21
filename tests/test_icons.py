# noqa: E501
import pytest

from tabler_icons.icons import IconDoesNotExists, extract_icon, get_icon


def test_extracts_icon() -> None:
    assert (
        extract_icon('arrow-narrow-right')
        == """
<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-arrow-narrow-right" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <line x1="5" y1="12" x2="19" y2="12" />
  <line x1="15" y1="16" x2="19" y2="12" />
  <line x1="15" y1="8" x2="19" y2="12" />
</svg>
""".strip()  #
    )


def test_raises_for_missing_icon() -> None:
    with pytest.raises(IconDoesNotExists, match='The icon _missing-icon does not exist.'):
        extract_icon('_missing-icon')


def test_get_icon() -> None:
    assert (
        get_icon('arrow-narrow-right')
        == """
<svg class="tabler-icon tabler-icon-arrow-narrow-right" width="20" height="20" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <line x1="5" y1="12" x2="19" y2="12" />
  <line x1="15" y1="16" x2="19" y2="12" />
  <line x1="15" y1="8" x2="19" y2="12" />
</svg>
""".strip()
    )


def test_get_icon_with_custom_size() -> None:
    assert (
        get_icon('arrow-narrow-right', 24)
        == """
<svg class="tabler-icon tabler-icon-arrow-narrow-right" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <line x1="5" y1="12" x2="19" y2="12" />
  <line x1="15" y1="16" x2="19" y2="12" />
  <line x1="15" y1="8" x2="19" y2="12" />
</svg>
""".strip()
    )


def test_get_icon_with_custom_svg_attributes() -> None:
    assert (
        get_icon('arrow-narrow-right', 24, style="color: red")
        == """
<svg class="tabler-icon tabler-icon-arrow-narrow-right" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round" style="color: red">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" />
  <line x1="5" y1="12" x2="19" y2="12" />
  <line x1="15" y1="16" x2="19" y2="12" />
  <line x1="15" y1="8" x2="19" y2="12" />
</svg>
""".strip()
    )


def test_get_icon_with_custom_path_attributes() -> None:
    assert (
        get_icon('arrow-narrow-right', 24, stroke_width=5)
        == """
<svg class="tabler-icon tabler-icon-arrow-narrow-right" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <path stroke="none" d="M0 0h24v24H0z" fill="none" stroke-width="5" />
  <line x1="5" y1="12" x2="19" y2="12" />
  <line x1="15" y1="16" x2="19" y2="12" />
  <line x1="15" y1="8" x2="19" y2="12" />
</svg>
""".strip()
    )
