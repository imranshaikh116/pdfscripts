import fitz  # PyMuPDF
import os

# === Folder Paths ===
input_folder = "input_pdfs"     # Folder with input PDFs
output_folder = "output_pdfs"   # Folder to save output PDFs
logo_path = "logo.png"          # Logo file

# === Settings ===
watermark_text = "ExamOS"
social_links = {
    "Instagram": "https://instagram.com/examos_original",
    "Telegram": "https://t.me/ExamOSoriginal"
}
telegram_link = "https://t.me/ExamOSoriginal"

font_size = 12
watermark_font_size = 30

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# === Loop through all PDFs in input folder ===
for file_name in os.listdir(input_folder):
    if not file_name.lower().endswith(".pdf"):
        continue  # skip non-PDFs

    pdf_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name)

    doc = fitz.open(pdf_path)

    for page in doc:
        width, height = page.rect.width, page.rect.height

        # --- Circles / Curved Gradient Background ---
        circle_positions = [
            (width * 0.2, height * 0.2),  # blue
            (width * 0.8, height * 0.3),  # pink
            (width * 0.5, height * 0.85)  # faint green (non-overlapping)
        ]
        circle_colors = [
            ((0.6, 0.8, 1), 0.20),   # blue
            ((1, 0.85, 0.9), 0.20),   # pink
            ((0.8, 1, 0.8), 0.20)    # faint green
        ]

        radius = min(width, height) * 0.4

        for (cx, cy), (color, opacity) in zip(circle_positions, circle_colors):
            rect = fitz.Rect(cx - radius, cy - radius, cx + radius, cy + radius)
            shape = page.new_shape()
            shape.draw_oval(rect)
            shape.finish(fill=color, fill_opacity=opacity, color=None)  # no border
            shape.commit()

        # --- Watermark Text ---
        page.insert_text(
            fitz.Point(width / 3, height / 2),
            watermark_text,
            fontsize=watermark_font_size,
            color=(0.5, 0.5, 0.5),
        )

        # --- Social Media Links ---
        y = height - 50
        for platform, url in social_links.items():
            text = f"{platform}: {url}"
            page.insert_text((40, y), text, fontsize=font_size, color=(0, 0, 0))
            link_rect = fitz.Rect(40, y, 300, y + 15)
            page.insert_link({
                "kind": fitz.LINK_URI,
                "from": link_rect,
                "uri": url
            })
            y += 20

        # --- Invisible Telegram Link (Excludes Bottom 60px to avoid overlap) ---
        safe_height = height - 60  # adjust if needed based on text placement
        page.insert_link({
        "kind": fitz.LINK_URI,
        "from": fitz.Rect(0, 0, width, safe_height),
        "uri": telegram_link
        })


        # --- Subtle Logo (Bottom-Right) ---
        try:
            img_rect = fitz.Rect(width - 70, height - 70, width - 14, height - 14)
            page.insert_image(img_rect, filename=logo_path, overlay=True, keep_proportion=True)

            # Add clickable Instagram link on logo area
            logo_link_rect = img_rect
            page.insert_link({
            "kind": fitz.LINK_URI,
            "from": logo_link_rect,
            "uri": social_links["Instagram"]
          })

        except Exception as e:
            print(f"⚠️ Could not insert logo on page {page.number + 1} of {file_name}: {e}")

    # Save processed PDF
    doc.save(output_path)
    doc.close()

    print(f"✅ Processed and saved: {output_path}")
