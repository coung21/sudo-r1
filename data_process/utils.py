import random
import re


def pretty_print_visual_elements(visual_elements: list) -> str:
    """
    Pretty print the visual elements.
    """
    out = []
    for c in visual_elements:
        ctype = c.get("type", "")
        
        if ctype == "lines":
            out.append(f"line, color: {c['color_name']}, coords: {' '.join(c['coords'])}")
        elif ctype == "arrows":
            out.append(f"arrow, color: {c['color_name']}, coords (base to tip): {' '.join(c['coords'])}")
        elif ctype in ("diagonal arrow", "horizontal arrow", "vertical arrow"):
            out.append(f"{ctype}, color: {c['color_name']}, in location: {c['coords'][0]}, pointing {c['direction']}")
        elif ctype in ("underlays", "overlays"):
            shape = f"shape: {c['shape']}" if c.get('shape') else ""
            text_val = str(c.get("text", "")).strip()
            text = f"text: {text_val}" if text_val else ""

            # color processing
            color_name = c.get("color_name", "")
            border_color_name = c.get("border_color_name", "")
            if color_name and border_color_name:
                if color_name == border_color_name:
                    color = f"color: {color_name}"
                else:
                    color = f"color: {color_name} (stroke color: {border_color_name})"
            elif color_name:
                color = f"color: {color_name}"
            elif border_color_name:
                color = f"stroke color: {border_color_name}"
            else:
                color = ""
            
            loc_type = c.get("loc", "")
            if loc_type == "cell":
                loc = f"location: {c['coords'][0]}"
            elif loc_type in ("vertical edge", "horizontal edge"):
                loc = f"location: between {c['coords'][0]} and {c['coords'][1]}"
            elif loc_type == "corner":
                loc = f"location: at the corner of {' '.join(c['coords'])}"
            else:
                loc = ""
            
            parts = [part for part in (text, shape, color, loc) if part]
            out.append(", ".join(parts))
        elif ctype == "inequality":
            out.append(f"inequality arrow: {c['direction']} between {c['cells'][0]} and {c['cells'][1]}")
        
        if ctype == "cage":
            if c.get("style", "") == "killer":
                if c.get("value", "") != "":
                    out.append(f"killer cage (value {c['value']}): {' '.join(c['cells'])}")
                else:
                    out.append(f"killer cage: {' '.join(c['cells'])}")
            elif c.get("style", "") == "box":
                if c.get("value", "") != "":
                    out.append(f"region (value {c['value']}): {' '.join(c['cells'])}")
                else:
                    out.append(f"region: {' '.join(c['cells'])}")

        if ctype == "global":
            out.append(f"global: {c['text']}")

        if ctype == "manual":
            out.append(f"{c['text']}")

    return "- " + "\n- ".join(out)

def format_sudoku_board(board_str):
    board_str = board_str.strip().replace("\n", "")
    if not board_str:
        raise ValueError("Empty board string")
    size = int(len(board_str) ** 0.5)
    
    # Format dạng grid text
    return '\n'.join(
        ' '.join(board_str[i:i+size]) for i in range(0, len(board_str), size)
    )



# import re

# def extract_answer(response_text: str) -> str:
#     match = re.search(r"<ANSWER>(.*?)</ANSWER>", response_text, re.DOTALL)
#     return match.group(1).strip() if match else ''

