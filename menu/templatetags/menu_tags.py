from django import template

from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, name):
    """Передача шаблона в дерево."""
    request = context['request']
    items = MenuItem.objects.filter(name=name).select_related('parent')
    tree = build_tree(items)
    current_path = request.path
    active_item = take_active_item(items, current_path)
    parents = get_parent_ids(active_item)
    children = get_children_ids(active_item)
    return {
        'menu': tree,
        'current_path': current_path,
        'parents': parents,
        'active_item': active_item,
        'children': children,
    }


def build_tree(items):
    """Создание пунктов меню."""
    lookup = {item.id: {'item': item, 'children': []} for item in items}
    roots = []
    for item in items:
        node = lookup[item.id]
        if item.parent_id and item.parent_id in lookup:
            lookup[item.parent_id]['children'].append(node)
        else:
            roots.append(node)
    return roots


def take_active_item(items, current_path):
    """Определение активного пункта меню."""
    active_item = None
    for item in items:
        if item.get_url() == current_path:
            active_item = item
            break
    return active_item


def get_parent_ids(active_item):
    """Проверка, является ли родитель активным пунктом меню."""
    parents_id = []
    while active_item and active_item.parent:
        parent = active_item.parent
        parents_id.append(parent.id)
        active_item = parent
    return parents_id


def get_children_ids(active_item):
    if not active_item:
        return []
    return [child.id for child in active_item.children.all()]
