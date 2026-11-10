import http.server
import socketserver
import json

print("🛰️ Booting Esosa's Local API Satellite Server... 🛰️")

PORT = 5000  # We will use port 5000 for our API data vault!

class APIDataHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 1. This is the raw data matrix package (JSON) we want to share!
        # It holds fake weather data and currency matrix info inside a dictionary.
        api_data_cabinet = {
            "status": "success",
            "weather": {
                "location": "Helmstedt, Germany",
                "temp_C": 12,
                "condition": "Cloudy with a Chance of Code ☁️"
            },
            "currency_rates": {
                "base": "USD",
                "EUR": 0.92,
                "GBP": 0.77,
                "JPY": 152.45
            }
        }
        
        # 2. Package headers telling the drone this is clean JSON data, not a webpage!
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        
        # 3. Transform our dictionary into a compressed text package and send it!
        json_string = json.dumps(api_data_cabinet)
        self.wfile.write(bytes(json_string, "utf-8"))

with socketserver.TCPServer(("", PORT), APIDataHandler) as httpd:
    print(f"🚀 SUCCESS! Local API vault is live and transmitting data at: http://localhost:{PORT}")
    print("Keep this terminal window open! Now we will write the bot to read it.")
    httpd.serve_forever()
