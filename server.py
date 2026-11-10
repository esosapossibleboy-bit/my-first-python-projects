import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

print("🌐 Initializing Esosa's Clean Analytical Web Server Core... 🌐")

PORT = 8000
visit_counter = 0

class MyWebServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global visit_counter
        
        parsed_url = urlparse(self.path)
        query_parameters = parse_qs(parsed_url.query)
        
        visitor_name = "Brave Hero"
        if "hero_name" in query_parameters:
            # 🌟 FIXED HERE: Adding [0] strips away the list brackets!
            visitor_name = query_parameters["hero_name"][0]
            
        visit_counter += 1

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
                .badge {{ background-color: gold; padding: 10px 20px; font-weight: bold; border-radius: 20px; display: inline-block; margin-bottom: 10px; }}
                .counter-box {{ background-color: #e0f7fa; border: 2px dashed darkcyan; padding: 15px; display: inline-block; font-size: 18px; font-weight: bold; border-radius: 10px; margin-top: 20px; color: darkcyan; }}
                input {{ padding: 10px; font-size: 16px; border-radius: 5px; border: 1px solid #ccc; width: 250px; }}
                button {{ padding: 10px 20px; font-size: 16px; background-color: darkblue; color: white; border: none; border-radius: 5px; cursor: pointer; }}
                button:hover {{ background-color: blue; }}
            </style>
        </head>
        <body>
            <h1>🌐 Welcome to Esosa's Live Web Server! 🌐</h1>
            <p>Salutations, <span style="color: purple; font-weight: bold;">{visitor_name}</span>! Welcome to your server node portal.</p>
            <div class="badge">🚀 Superpower Unlocked: Server State Management</div>
            
            <br>
            <div class="counter-box">
                📊 Total Portal Hits Tracked: {visit_counter}
            </div>
            
            <div style="margin-top: 30px;">
                <form method="GET" action="/">
                    <input type="text" name="hero_name" placeholder="Type your hero name here..." required>
                    <button type="submit">Cast Portal Spell! ✨</button>
                </form>
            </div>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(html_blueprint, "utf-8"))

with socketserver.TCPServer(("", PORT), MyWebServer) as httpd:
    print(f"🚀 SUCCESS! Your analytics server is live at: http://localhost:{PORT}")
    print("Press Ctrl + C in the terminal when you want to stop the server.")
    httpd.serve_forever()
