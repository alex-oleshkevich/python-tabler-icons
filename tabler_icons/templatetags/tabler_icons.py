from __future__ import annotations

import typing
from django import template
from django.utils.safestring import SafeString, mark_safe

from ..icons import get_icon

register = template.Library()


@register.simple_tag
def tabler_icon(name: str, size: typing.Union[str, int] = 24, **svg_attrs: object) -> str:
    fixed_kwargs = {key: (value + "" if isinstance(value, SafeString) else value) for key, value in svg_attrs.items()}
    return mark_safe(get_icon(name, size, **fixed_kwargs))
