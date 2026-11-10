import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

print("🌐 Initializing Esosa's Interactive Web Server Core... 🌐")

PORT = 8000

# 🚀 THE UPDATED MAGIC CORE FUNCTION
class MyWebServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 1. Parse the incoming URL drone data to check for any trailing data train cars!
        parsed_url = urlparse(self.path)
        query_parameters = parse_qs(parsed_url.query)
        
        # Default name if the box is empty
        visitor_name = "Brave Hero"
        
        # 2. If 'hero_name' is hiding inside the URL train, scoop it out!
        if "hero_name" in query_parameters:
            visitor_name = query_parameters["hero_name"][0]

        # 3. Build our dynamic HTML template on the fly using our parsed name!
        html_blueprint = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Esosa's Cloud Server</title>
            <style>
                body {{ font-family: Arial, sans-serif; text-align: center; background-color: #f0f8ff; padding-top: 50px; }}
                h1 {{ color: darkblue; font-size: 40px; }}
                p {{ font-size: 20px; color: #333; }}
                .badge {{ background-color: gold; padding: 10px 20px; font-weight: bold; border-radius: 20px; display: inline-block; margin-bottom: 20px; }}
                input {{ padding: 10px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc; width: 250px; }}
                button {{ padding: 10px 20px; font-size: 16px; background-color: darkblue; color: white; border: none; border-radius: 5px; cursor: pointer; }}
                button:hover {{ background-color: blue; }}
            </style>
        </head>
        <body>
            <h1>🌐 Welcome to Esosa's Live Web Server! 🌐</h1>
            <p>Salutations, <span style="color: purple; font-weight: bold;">{visitor_name}</span>! Welcome to your server node portal.</p>
            <div class="badge">🚀 Superpower Unlocked: Full-Stack Routing</div>
            
            <!-- 🌟 THE INPUT WEB FORM SECTION 🌟 -->
            <div style="margin-top: 30px;">
                <form method="GET" action="/">
                    <input type="text" name="hero_name" placeholder="Type your hero name here..." required>
                    <button type="submit">Cast Portal Spell! ✨</button>
                </form>
            </div>
        </body>
        </html>
        """

        # 4. Ship the response package down the pipe to the browser
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html_blueprint, "utf-8"))

# Run the backend engine listening loop
with socketserver.TCPServer(("", PORT), MyWebServer) as httpd:
    print(f"🚀 SUCCESS! Your web server is live at: http://localhost:{PORT}")
    print("Press Ctrl + C in the terminal when you want to stop the server.")
    httpd.serve_forever()
