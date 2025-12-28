#!/usr/bin/env python3
"""
👂 The Listening Server
I sit here and wait for people to talk to me. 🛋️
I am the Chat Bot host!
"""

import socket

class ChatServer:
    def start_server(self, host='127.0.0.1', port=9999):
        print("\n--- 🎧 Startup Server ---")
        try:
            # 1️⃣ Create Socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # 2️⃣ Bind to Address (Claim the IP and Port)
            # '127.0.0.1' = Localhost (Only this computer can connect)
            s.bind((host, port))
            print(f"   📍 Bound to {host}:{port}")
            
            # 3️⃣ Listen (Wait for calls)
            s.listen(1)
            print("   ⏳ Waiting for incoming connection...")
            
            while True:
                # 4️⃣ Accept Connection
                client_socket, addr = s.accept()
                print(f"   🎉 Got connection from {addr}!")
                
                try:
                    while True:
                        # 5️⃣ Receive Data
                        data = client_socket.recv(1024)
                        
                        if not data:
                            print(f"   👋 Client {addr} disconnected.")
                            break
                        
                        decoded = data.decode('utf-8')
                        print(f"   📩 Received: '{decoded}'")
                        
                        # 6️⃣ Send Echo Reply
                        reply = f"ACK: I heard '{decoded}'"
                        client_socket.send(reply.encode('utf-8'))
                        
                finally:
                    client_socket.close()
                    print("   🔒 Connection closed. Waiting for next...")
                    
        except KeyboardInterrupt:
            print("\n   🛑 Server stopping...")
        except Exception as ex:
            print(f"   ❌ Error: {ex}")
        finally:
            if 's' in locals():
                s.close()

if __name__ == "__main__":
    server = ChatServer()
    server.start_server()
