import os

# Создаем папку для файлов
output_dir = "w3school"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Функция для генерации идеальной структуры HTML
def create_page(body_content, head_content="", title="W3Schools Example"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    {head_content}
</head>
<body>

{body_content}

</body>
</html>"""

# Словарь с контентом. 
# 'body': то, что внутри <body>
# 'head': (опционально) то, что внутри <head> (например, стили)
pages_data = {
    "01_html_home.html": {
        "title": "HTML Home",
        "body": """
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
        """
    },
    "02_html_intro.html": {
        "title": "HTML Introduction",
        "body": """
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
        """
    },
    "03_html_editors.html": {
        "title": "HTML Editors",
        "body": """
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
        """
    },
    "04_html_basic.html": {
        "title": "HTML Basic",
        "body": """
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>

    <hr>

    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>

    <p>This is a paragraph.</p>
    <p>This is another paragraph.</p>

    <a href="https://www.w3schools.com">This is a link</a>
    <br>

    <img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142">
        """
    },
    "05_html_elements.html": {
        "title": "HTML Elements",
        "body": """
    <h1>My First Heading</h1>
    <p>My first paragraph.</p>
    
    <p>This is a <br> paragraph with a line break.</p>
        """
    },
    "06_html_attributes.html": {
        "title": "HTML Attributes",
        "body": """
    <a href="https://www.w3schools.com">Visit W3Schools</a>
    <br><br>

    <img src="img_girl.jpg" width="500" height="600" alt="Girl with a jacket">
    <br>

    <p style="color:red;">This is a red paragraph.</p>

    <p title="I'm a tooltip">Hover over this paragraph.</p>
        """
    },
    "07_html_headings.html": {
        "title": "HTML Headings",
        "body": """
    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    <h5>Heading 5</h5>
    <h6>Heading 6</h6>

    <h1 style="font-size:60px;">Heading 1 (Bigger)</h1>
        """
    },
    "08_html_paragraphs.html": {
        "title": "HTML Paragraphs",
        "body": """
    <p>This is a paragraph.</p>
    <p>This is another paragraph.</p>

    <hr>
    <h1>This is heading 1</h1>
    <p>This is some text.</p>
    <hr>
    <h2>This is heading 2</h2>
    <p>This is some other text.</p>
    <hr>

    <p>This is<br>a paragraph<br>with line breaks.</p>

    <pre>
      My Bonnie lies over the ocean.
      My Bonnie lies over the sea.
      My Bonnie lies over the ocean.
      Oh, bring back my Bonnie to me.
    </pre>
        """
    },
    "09_html_styles.html": {
        "title": "HTML Styles",
        "body": """
    <div style="background-color:powderblue; padding: 20px;">
        <p>Simulated body background color.</p>
    </div>

    <h1 style="color:blue;">This is a heading</h1>
    <p style="color:red;">This is a paragraph.</p>

    <h1 style="font-family:verdana;">This is a heading</h1>
    <p style="font-family:courier;">This is a paragraph.</p>

    <h1 style="font-size:300%;">This is a heading</h1>
    <p style="font-size:160%;">This is a paragraph.</p>

    <h1 style="text-align:center;">Centered Heading</h1>
    <p style="text-align:center;">Centered paragraph.</p>
        """
    },
    "10_html_formatting.html": {
        "title": "HTML Formatting",
        "body": """
    <p><b>This text is bold</b></p>
    <p><strong>This text is important!</strong></p>
    <p><i>This text is italic</i></p>
    <p><em>This text is emphasized</em></p>
    <p><small>This is some smaller text.</small></p>
    <p>Do not forget to buy <mark>milk</mark> today.</p>
    <p>My favorite color is <del>blue</del> red.</p>
    <p>My favorite color is <del>blue</del> <ins>red</ins>.</p>
    <p>This is <sub>subscripted</sub> text.</p>
    <p>This is <sup>superscripted</sup> text.</p>
        """
    },
    "11_html_quotations.html": {
        "title": "HTML Quotations",
        "body": """
    <p>Here is a quote from WWF's website:</p>
    <blockquote cite="http://www.worldwildlife.org/who/index.html">
    For 50 years, WWF has been protecting the future of nature.
    The world's leading conservation organization, WWF works in 100 countries...
    </blockquote>

    <p>WWF's goal is to: <q>Build a future where people live in harmony with nature.</q></p>

    <p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>

    <address>
    Written by John Doe.<br>
    Visit us at:<br>
    Example.com<br>
    Box 564, Disneyland<br>
    USA
    </address>

    <p><cite>The Scream</cite> by Edvard Munch. Painted in 1893.</p>

    <bdo dir="rtl">This text will be written from right to left</bdo>
        """
    },
    "12_html_comments.html": {
        "title": "HTML Comments",
        "body": """
    <p>This is a paragraph.</p>

    """
    },
    "13_html_colors.html": {
        "title": "HTML Colors",
        "body": """
    <h1 style="background-color:DodgerBlue;">Hello World</h1>
    <p style="background-color:Tomato;">Lorem ipsum...</p>

    <h1 style="color:Tomato;">Hello World</h1>
    <p style="color:DodgerBlue;">Lorem ipsum...</p>
    <p style="color:MediumSeaGreen;">Ut wisi enim...</p>

    <h1 style="border:2px solid Tomato;">Hello World</h1>
    <h1 style="border:2px solid DodgerBlue;">Hello World</h1>
    <h1 style="border:2px solid Violet;">Hello World</h1>

    <h1 style="background-color:rgb(255, 99, 71);">RGB</h1>
    <h1 style="background-color:#ff6347;">HEX</h1>
    <h1 style="background-color:hsl(9, 100%, 64%);">HSL</h1>

    <h1 style="background-color:rgba(255, 99, 71, 0.5);">RGBA (Transparent)</h1>
    <h1 style="background-color:hsla(9, 100%, 64%, 0.5);">HSLA (Transparent)</h1>
        """
    },
    "14_html_css.html": {
        "title": "HTML CSS",
        "head": """
    <style>
    /* Internal CSS Example */
    .internal-css-demo {
        background-color: powderblue;
        padding: 10px;
    }
    .internal-css-demo h1 {
        color: blue;
    }
    .internal-css-demo p {
        color: red;
        border: 2px solid powderblue;
        padding: 30px;
        margin: 50px;
    }
    </style>
    <link rel="stylesheet" href="styles.css">
        """,
        "body": """
    <h1 style="color:blue;">A Blue Heading (Inline)</h1>
    <p style="color:red;">A red paragraph (Inline).</p>

    <hr>
    
    <div class="internal-css-demo">
        <h1>This is a heading (Internal CSS)</h1>
        <p>This is a paragraph (Internal CSS).</p>
    </div>
        """
    },
    "15_html_links.html": {
        "title": "HTML Links",
        "body": """
    <p><a href="https://www.w3schools.com/">Visit W3Schools.com!</a></p>

    <p><a href="https://www.w3schools.com/" target="_blank">Visit W3Schools (New Tab)!</a></p>

    <p>Image as a link: <br>
    <a href="default.asp">
        <img src="smiley.gif" alt="HTML tutorial" style="width:42px;height:42px;">
    </a>
    </p>

    <p><a href="mailto:someone@example.com">Send email</a></p>

    <p><a href="https://www.w3schools.com/html/" title="Go to W3Schools HTML section">Visit our HTML Tutorial (Tooltip)</a></p>
        """
    },
    "16_html_images.html": {
        "title": "HTML Images",
        "body": """
    <img src="img_chania.jpg" alt="Flowers in Chania">
    <br>

    <img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">
    <br>

    <img src="img_girl.jpg" alt="Girl in a jacket" style="width:500px;height:600px;">
    <br>

    <p>
        <img src="smiley.gif" alt="Smiley face" style="float:right;width:42px;height:42px;">
        The image will float to the right of this text.
    </p>
        """
    },
    "17_html_favicon.html": {
        "title": "HTML Favicon",
        "head": """
    <link rel="icon" type="image/x-icon" href="/images/favicon.ico">
        """,
        "body": """
    <h1>This Page has a Favicon</h1>
    <p>Look at the browser tab to see the icon.</p>
        """
    },
    "18_html_page_title.html": {
        "title": "HTML Page Title Tutorial",
        "body": """
    <h1>Check the Browser Tab</h1>
    <p>The title of this document is "HTML Page Title Tutorial".</p>
        """
    },
    "19_html_tables.html": {
        "title": "HTML Tables",
        "head": """
    <style>
    table, th, td {
      border: 1px solid black;
      border-collapse: collapse;
      padding: 5px;
    }
    </style>
        """,
        "body": """
    <h2>Basic Table</h2>
    <table style="width:100%">
      <tr>
        <th>Company</th>
        <th>Contact</th>
        <th>Country</th>
      </tr>
      <tr>
        <td>Alfreds Futterkiste</td>
        <td>Maria Anders</td>
        <td>Germany</td>
      </tr>
      <tr>
        <td>Centro comercial Moctezuma</td>
        <td>Francisco Chang</td>
        <td>Mexico</td>
      </tr>
    </table>
        """
    },
    "20_html_lists.html": {
        "title": "HTML Lists",
        "body": """
    <h2>Unordered List</h2>
    <ul>
      <li>Coffee</li>
      <li>Tea</li>
      <li>Milk</li>
    </ul>

    <h2>Ordered List</h2>
    <ol>
      <li>Coffee</li>
      <li>Tea</li>
      <li>Milk</li>
    </ol>

    <h2>Description List</h2>
    <dl>
      <dt>Coffee</dt>
      <dd>- black hot drink</dd>
      <dt>Milk</dt>
      <dd>- white cold drink</dd>
    </dl>
        """
    },
    "21_html_blocks.html": {
        "title": "HTML Block and Inline",
        "body": """
    <h2>Block Element (div)</h2>
    <div style="background-color:black;color:white;padding:20px;">
      <h3>London</h3>
      <p>London is the capital city of England.</p>
    </div>

    <h2>Inline Element (span)</h2>
    <p>My mother has <span style="color:blue;font-weight:bold;">blue</span> eyes.</p>
        """
    },
    "22_html_div.html": {
        "title": "HTML Div",
        "head": """
    <style>
    .centered-div {
      width: 300px;
      margin: auto;
      border: 1px solid red;
      padding: 10px;
    }
    </style>
        """,
        "body": """
    <h2>Div Container</h2>
    <div>
      <h3>London</h3>
      <p>London is the capital city of England.</p>
    </div>

    <h2>Div with Margin Auto (Centered)</h2>
    <div class="centered-div">
      <h3>London (Centered)</h3>
      <p>London is the capital city of England.</p>
    </div>
        """
    },
    "23_html_classes.html": {
        "title": "HTML Classes",
        "head": """
    <style>
    .city {
      background-color: tomato;
      color: white;
      border: 2px solid black;
      margin: 20px;
      padding: 20px;
    }
    .main {
        text-align: center;
    }
    </style>
        """,
        "body": """
    <div class="city">
      <h2>London</h2>
      <p>London is the capital of England.</p>
    </div>

    <h2 class="city main">Paris (Multiple Classes)</h2>
        """
    },
    "24_html_id.html": {
        "title": "HTML Id",
        "head": """
    <style>
    #myHeader {
      background-color: lightblue;
      color: black;
      padding: 40px;
      text-align: center;
    }
    </style>
        """,
        "body": """
    <h1 id="myHeader">My Header</h1>

    <p><a href="#C4">Jump to Chapter 4</a></p>
    
    <div style="height:800px; background-color: #f0f0f0; padding:10px;">
        (Spacer for scrolling)
    </div>

    <h2 id="C4">Chapter 4</h2>
    <p>This is chapter 4.</p>
        """
    }
}

# Генерация файлов
for filename, content in pages_data.items():
    file_path = os.path.join(output_dir, filename)
    
    # Собираем полный HTML
    full_html = create_page(
        body_content=content["body"].strip(),
        head_content=content.get("head", "").strip(),
        title=content["title"]
    )
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Created correct file: {filename}")

print(f"\nГотово! Все исправленные файлы находятся в папке '{output_dir}'.")