#!/usr/bin/env python3
"""
💬 The Chatty Client
I connect to a server and send messages!
Make sure the Server is running first! 🏃
"""

import socket

class ChatClient:
    def connect_to_server(self, host='127.0.0.1', port=1234):
        print("\n--- 🔌 Connecting to Server ---")
        print(f"   Target: {host}:{port}")
        
        try:
            # 1️⃣ Create Socket (IPv4, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # 2️⃣ Connect
            s.connect((host, port))
            print("   ✅ Connected! Type 'exit' to quit.\n")
            
            # 3️⃣ Chat Loop
            while True:
                msg = input("   👉 You say: ")
                
                if not msg or msg.lower() == 'exit':
                    print("   👋 Leaving chat.")
                    break
                
                # Send (Encode to bytes)
                s.send(msg.encode('utf-8'))
                
                # Receive Reply (Decode to string)
                reply = s.recv(1024).decode('utf-8')
                print(f"   🤖 Server says: {reply}")
                
            s.close()
            
        except ConnectionRefusedError:
            print("   ❌ Connection Failed! Is the server running?")
        except Exception as ex:
            print(f"   ❌ Error: {ex}")

if __name__ == "__main__":
    client = ChatClient()
    # Using localhost for testing
    client.connect_to_server('127.0.0.1', 9999) 
