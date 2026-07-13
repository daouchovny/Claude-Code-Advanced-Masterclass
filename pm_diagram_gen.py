#!/usr/bin/env python3
"""
PM Diagram Generator
Professional diagram generation for Product Managers
Supports: User Journey Maps, Technical Architecture Diagrams
"""

import argparse
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import math

# Color themes
THEMES = {
    'default': {
        'background': '#1a1a2e',
        'card_bg': '#16213e',
        'primary': '#0f3460',
        'accent': '#e94560',
        'highlight': '#4fd1c5',
        'secondary': '#6d28d9',
        'success': '#10b981',
        'warning': '#f59e0b',
        'text_white': '#ffffff',
        'text_light': '#a8a8a8',
        'text_dark': '#374151',
        'connector': '#4fd1c5'
    },
    'dark': {
        'background': '#0f0f0f',
        'card_bg': '#1f1f1f',
        'primary': '#2d2d2d',
        'accent': '#ff6b6b',
        'highlight': '#4ecdc4',
        'secondary': '#7c3aed',
        'success': '#22c55e',
        'warning': '#eab308',
        'text_white': '#ffffff',
        'text_light': '#9ca3af',
        'text_dark': '#374151',
        'connector': '#4ecdc4'
    },
    'light': {
        'background': '#f8fafc',
        'card_bg': '#ffffff',
        'primary': '#e2e8f0',
        'accent': '#dc2626',
        'highlight': '#0891b2',
        'secondary': '#6d28d9',
        'success': '#16a34a',
        'warning': '#ca8a04',
        'text_white': '#1e293b',
        'text_light': '#64748b',
        'text_dark': '#1e293b',
        'connector': '#0891b2'
    },
    'corporate': {
        'background': '#1e3a5f',
        'card_bg': '#2d4a6f',
        'primary': '#3d5a80',
        'accent': '#ee6c4d',
        'highlight': '#98c1d9',
        'secondary': '#5b21b6',
        'success': '#57cc99',
        'warning': '#ffd166',
        'text_white': '#ffffff',
        'text_light': '#c9d6df',
        'text_dark': '#293241',
        'connector': '#98c1d9'
    }
}

def get_fonts():
    """Load system fonts with fallbacks"""
    try:
        return {
            'title': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 42),
            'heading': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28),
            'body': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18),
            'small': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14),
            'icon': ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        }
    except:
        default = ImageFont.load_default()
        return {k: default for k in ['title', 'heading', 'body', 'small', 'icon']}


def draw_rounded_rect(draw, coords, radius, fill, outline=None, width=1):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = coords
    draw.rounded_rectangle(coords, radius=radius, fill=fill, outline=outline, width=width)


def draw_arrow(draw, start, end, color, width=2):
    """Draw an arrow between two points"""
    draw.line([start, end], fill=color, width=width)
    # Arrowhead
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    arrow_length = 12
    arrow_angle = math.pi / 6

    x1 = end[0] - arrow_length * math.cos(angle - arrow_angle)
    y1 = end[1] - arrow_length * math.sin(angle - arrow_angle)
    x2 = end[0] - arrow_length * math.cos(angle + arrow_angle)
    y2 = end[1] - arrow_length * math.sin(angle + arrow_angle)

    draw.polygon([end, (x1, y1), (x2, y2)], fill=color)


def generate_user_journey(title, subtitle, stages, touchpoints, emotions, actions, theme_name, output):
    """Generate a user journey map"""
    colors = THEMES.get(theme_name, THEMES['default'])
    fonts = get_fonts()

    num_stages = len(stages)
    width = max(1400, 250 * num_stages)
    height = 900

    img = Image.new('RGB', (width, height), colors['background'])
    draw = ImageDraw.Draw(img)

    # Header
    draw.rectangle([0, 0, width, 100], fill=colors['card_bg'])
    draw.text((width//2, 35), title.upper(), font=fonts['title'], fill=colors['text_white'], anchor="mm")
    if subtitle:
        draw.text((width//2, 75), subtitle, font=fonts['body'], fill=colors['text_light'], anchor="mm")

    # Accent line
    draw.rectangle([80, 105, width-80, 110], fill=colors['accent'])

    # Stage columns
    stage_width = (width - 160) // num_stages
    stage_colors = [colors['accent'], colors['highlight'], colors['secondary'],
                    colors['success'], colors['warning'], colors['primary']]

    y_start = 140

    # Draw stage headers and content
    for i, stage in enumerate(stages):
        x_start = 80 + i * stage_width
        x_center = x_start + stage_width // 2
        color = stage_colors[i % len(stage_colors)]

        # Stage number circle
        draw.ellipse([x_center-20, y_start, x_center+20, y_start+40], fill=color)
        draw.text((x_center, y_start+20), str(i+1), font=fonts['body'], fill=colors['text_white'], anchor="mm")

        # Stage name
        draw.text((x_center, y_start+60), stage, font=fonts['heading'], fill=colors['text_white'], anchor="mm")

        # Connector arrow (except for last stage)
        if i < num_stages - 1:
            arrow_start = (x_start + stage_width - 30, y_start + 20)
            arrow_end = (x_start + stage_width + 30, y_start + 20)
            draw_arrow(draw, arrow_start, arrow_end, colors['connector'], 3)

    # Sections
    sections = [
        ("TOUCHPOINTS", touchpoints, colors['card_bg']),
        ("EMOTIONS", emotions, colors['primary']),
        ("ACTIONS", actions, colors['card_bg'])
    ]

    section_y = y_start + 100
    section_height = 180

    for section_name, items, bg_color in sections:
        # Section label
        draw.text((40, section_y + section_height//2), section_name, font=fonts['small'],
                  fill=colors['text_light'], anchor="lm")

        # Section content for each stage
        for i in range(num_stages):
            x_start = 80 + i * stage_width
            x_end = x_start + stage_width - 10

            draw_rounded_rect(draw, [x_start+5, section_y+5, x_end, section_y+section_height-5],
                            radius=10, fill=bg_color)

            if i < len(items):
                # Word wrap the text
                item_text = items[i] if items[i] else "-"
                words = item_text.split()
                lines = []
                current_line = ""
                max_width = stage_width - 40

                for word in words:
                    test_line = f"{current_line} {word}".strip()
                    bbox = draw.textbbox((0, 0), test_line, font=fonts['body'])
                    if bbox[2] - bbox[0] <= max_width:
                        current_line = test_line
                    else:
                        if current_line:
                            lines.append(current_line)
                        current_line = word
                if current_line:
                    lines.append(current_line)

                text_y = section_y + 25
                for line in lines[:5]:  # Max 5 lines
                    draw.text((x_start + 20, text_y), line, font=fonts['body'], fill=colors['text_white'])
                    text_y += 25

        section_y += section_height + 10

    # Footer
    draw.rectangle([0, height-50, width, height], fill=colors['card_bg'])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    draw.text((width//2, height-25), f"Generated: {timestamp}  |  PM Diagrams Skill",
              font=fonts['small'], fill=colors['text_light'], anchor="mm")

    # Save
    output_path = output or f"user_journey_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img.save(output_path, 'PNG', quality=95)
    print(f"✓ User Journey Map saved to: {output_path}")
    return output_path


def generate_architecture(title, subtitle, components, connections, layers, theme_name, output):
    """Generate a technical architecture diagram"""
    colors = THEMES.get(theme_name, THEMES['default'])
    fonts = get_fonts()

    num_components = len(components)
    width = 1400
    height = max(900, 150 * ((num_components // 4) + 1) + 400)

    img = Image.new('RGB', (width, height), colors['background'])
    draw = ImageDraw.Draw(img)

    # Header
    draw.rectangle([0, 0, width, 100], fill=colors['card_bg'])
    draw.text((width//2, 35), title.upper(), font=fonts['title'], fill=colors['text_white'], anchor="mm")
    if subtitle:
        draw.text((width//2, 75), subtitle, font=fonts['body'], fill=colors['text_light'], anchor="mm")

    draw.rectangle([80, 105, width-80, 110], fill=colors['accent'])

    # Component colors by type
    component_colors = {
        'frontend': colors['highlight'],
        'backend': colors['primary'],
        'database': colors['secondary'],
        'api': colors['accent'],
        'service': colors['success'],
        'external': colors['warning'],
        'default': colors['card_bg']
    }

    # Calculate grid layout
    cols = min(4, num_components)
    rows = math.ceil(num_components / cols)

    comp_width = 280
    comp_height = 120
    h_spacing = (width - 160 - cols * comp_width) // (cols + 1)
    v_spacing = 40

    start_y = 150
    component_positions = {}

    # Draw layers if provided
    if layers:
        layer_height = (rows * (comp_height + v_spacing)) // len(layers)
        for i, layer in enumerate(layers):
            y = start_y + i * layer_height - 20
            draw.rectangle([60, y, width-60, y + layer_height], fill=colors['card_bg'], outline=colors['primary'])
            draw.text((70, y + 10), layer.upper(), font=fonts['small'], fill=colors['text_light'])

    # Draw components
    for i, comp in enumerate(components):
        row = i // cols
        col = i % cols

        x = 80 + h_spacing + col * (comp_width + h_spacing)
        y = start_y + row * (comp_height + v_spacing) + 30

        # Determine component type for coloring
        comp_lower = comp.lower()
        if any(k in comp_lower for k in ['web', 'app', 'ui', 'frontend', 'client']):
            comp_type = 'frontend'
        elif any(k in comp_lower for k in ['db', 'database', 'postgres', 'mongo', 'redis', 'cache']):
            comp_type = 'database'
        elif any(k in comp_lower for k in ['api', 'gateway', 'rest', 'graphql']):
            comp_type = 'api'
        elif any(k in comp_lower for k in ['service', 'worker', 'queue']):
            comp_type = 'service'
        elif any(k in comp_lower for k in ['external', 'third', '3rd', 'integration']):
            comp_type = 'external'
        else:
            comp_type = 'backend'

        color = component_colors.get(comp_type, component_colors['default'])

        # Draw component box
        draw_rounded_rect(draw, [x, y, x + comp_width, y + comp_height],
                         radius=15, fill=color, outline=colors['text_white'], width=2)

        # Component icon based on type
        icons = {
            'frontend': '[ ]',
            'backend': '{...}',
            'database': '[=]',
            'api': '</>',
            'service': '(S)',
            'external': '[E]'
        }
        icon = icons.get(comp_type, '[ ]')
        draw.text((x + 15, y + 15), icon, font=fonts['icon'], fill=colors['text_white'])

        # Component name
        draw.text((x + comp_width//2, y + comp_height//2 + 10), comp,
                  font=fonts['heading'], fill=colors['text_white'], anchor="mm")

        # Store position for connections
        component_positions[comp] = {
            'center': (x + comp_width//2, y + comp_height//2),
            'top': (x + comp_width//2, y),
            'bottom': (x + comp_width//2, y + comp_height),
            'left': (x, y + comp_height//2),
            'right': (x + comp_width, y + comp_height//2)
        }

    # Draw connections
    if connections:
        for conn in connections:
            parts = conn.split('->')
            if len(parts) == 2:
                from_comp = parts[0].strip()
                to_comp = parts[1].strip()

                if from_comp in component_positions and to_comp in component_positions:
                    from_pos = component_positions[from_comp]['right']
                    to_pos = component_positions[to_comp]['left']

                    # Adjust based on relative positions
                    from_center = component_positions[from_comp]['center']
                    to_center = component_positions[to_comp]['center']

                    if abs(from_center[0] - to_center[0]) < comp_width:
                        # Vertical connection
                        if from_center[1] < to_center[1]:
                            from_pos = component_positions[from_comp]['bottom']
                            to_pos = component_positions[to_comp]['top']
                        else:
                            from_pos = component_positions[from_comp]['top']
                            to_pos = component_positions[to_comp]['bottom']

                    draw_arrow(draw, from_pos, to_pos, colors['connector'], 2)

    # Legend
    legend_y = height - 120
    draw.rectangle([0, legend_y, width, height], fill=colors['card_bg'])
    draw.text((80, legend_y + 15), "LEGEND:", font=fonts['body'], fill=colors['text_white'])

    legend_items = [
        ('Frontend/UI', 'frontend'),
        ('API/Gateway', 'api'),
        ('Service', 'service'),
        ('Database', 'database'),
        ('External', 'external')
    ]

    legend_x = 180
    for name, comp_type in legend_items:
        color = component_colors.get(comp_type, colors['card_bg'])
        draw.rectangle([legend_x, legend_y + 12, legend_x + 20, legend_y + 32], fill=color)
        draw.text((legend_x + 30, legend_y + 15), name, font=fonts['small'], fill=colors['text_light'])
        legend_x += 180

    # Timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    draw.text((width//2, legend_y + 70), f"Generated: {timestamp}  |  PM Diagrams Skill",
              font=fonts['small'], fill=colors['text_light'], anchor="mm")

    # Save
    output_path = output or f"architecture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    img.save(output_path, 'PNG', quality=95)
    print(f"✓ Architecture Diagram saved to: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description='PM Diagram Generator')
    subparsers = parser.add_subparsers(dest='command', help='Diagram type')

    # User Journey subcommand
    journey_parser = subparsers.add_parser('journey', help='Generate user journey map')
    journey_parser.add_argument('--title', required=True, help='Journey title')
    journey_parser.add_argument('--subtitle', default='', help='Subtitle/description')
    journey_parser.add_argument('--stages', required=True, help='Comma-separated journey stages')
    journey_parser.add_argument('--touchpoints', default='', help='Comma-separated touchpoints per stage')
    journey_parser.add_argument('--emotions', default='', help='Comma-separated emotions per stage')
    journey_parser.add_argument('--actions', default='', help='Comma-separated actions per stage')
    journey_parser.add_argument('--theme', default='default', choices=THEMES.keys(), help='Color theme')
    journey_parser.add_argument('--output', help='Output filename')

    # Architecture subcommand
    arch_parser = subparsers.add_parser('architecture', help='Generate architecture diagram')
    arch_parser.add_argument('--title', required=True, help='Diagram title')
    arch_parser.add_argument('--subtitle', default='', help='Subtitle/description')
    arch_parser.add_argument('--components', required=True, help='Comma-separated components')
    arch_parser.add_argument('--connections', default='', help='Connections (e.g., "A->B,B->C")')
    arch_parser.add_argument('--layers', default='', help='Layer names (e.g., "Frontend,Backend,Data")')
    arch_parser.add_argument('--theme', default='default', choices=THEMES.keys(), help='Color theme')
    arch_parser.add_argument('--output', help='Output filename')

    args = parser.parse_args()

    if args.command == 'journey':
        stages = [s.strip() for s in args.stages.split(',')]
        touchpoints = [t.strip() for t in args.touchpoints.split(',')] if args.touchpoints else [''] * len(stages)
        emotions = [e.strip() for e in args.emotions.split(',')] if args.emotions else [''] * len(stages)
        actions = [a.strip() for a in args.actions.split(',')] if args.actions else [''] * len(stages)

        generate_user_journey(
            title=args.title,
            subtitle=args.subtitle,
            stages=stages,
            touchpoints=touchpoints,
            emotions=emotions,
            actions=actions,
            theme_name=args.theme,
            output=args.output
        )

    elif args.command == 'architecture':
        components = [c.strip() for c in args.components.split(',')]
        connections = [c.strip() for c in args.connections.split(',')] if args.connections else []
        layers = [l.strip() for l in args.layers.split(',')] if args.layers else []

        generate_architecture(
            title=args.title,
            subtitle=args.subtitle,
            components=components,
            connections=connections,
            layers=layers,
            theme_name=args.theme,
            output=args.output
        )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
