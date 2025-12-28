#!/usr/bin/env python3
"""
🏊‍♂️ The Worker Pool
Using a pool of processes to crunch data in parallel!
It's like having a team of writers scribbling at the same time! ✍️
"""

import multiprocessing as mp
import datetime as dt
import time

class FastWriter:
    
    def write_task(self, file_label):
        """
        Writes a bunch of lines to a file.
        This is the task we want to speed up! 🏎️
        """
        try:
            start_t = dt.datetime.now()
            process_name = mp.current_process().name
            
            print(f"   🚀 [{process_name}] Started writing '{file_label}'...")
            
            filename = f"{file_label}.txt"
            
            # 📝 Writing to file
            with open(filename, "w+") as out_file:
                out_file.write("Process_name, ID, Time\n")
                
                # Reducing count to 10,000 for demo speed (Original was 1,000,000!)
                for i in range(10000): 
                    # Simulating work
                    line = f"{process_name}, {i}, {dt.datetime.now()}\n"
                    out_file.write(line)
            
            end_t = dt.datetime.now()
            duration = (end_t - start_t).total_seconds()
            
            print(f"   ✅ [{process_name}] Done! (Took {duration}s)")
            return f"📄 {file_label}: Success ({duration}s)"
            
        except Exception as ex:
            return f"❌ {file_label}: Failed ({ex})"

    def run_pool_demo(self):
        """
        Manages the Pool of workers.
        """
        print("\n--- 🏊‍♂️ Starting Pool Party ---")
        
        try:
            start_main = dt.datetime.now()
            
            # 1️⃣ Check Hardware
            cpu_count = mp.cpu_count()
            print(f"   🖥️  CPU Cores Available: {cpu_count}")
            
            # 2️⃣ Create the Pool
            # We create a pool as big as our CPU count
            pool = mp.Pool(cpu_count)
            results = []
            
            # 3️⃣ Assign Tasks (Asynchronously)
            # apply_async means "Go do this, and let me know when you're done"
            print("   📨 Distributing tasks...")
            for i in range(8):
                task_name = f"Data_Chunk_{i}"
                res = pool.apply_async(self.write_task, args=(task_name,))
                results.append(res)
            
            # 4️⃣ Close & Join
            # Close: No more new tasks
            # Join: Wait for current tasks to finish
            print("   🔒 Pool Closed. Waiting for swimmers...")
            pool.close()
            pool.join()
            
            end_main = dt.datetime.now()
            
            # 5️⃣ Report Results
            print("\n--- 📊 Final Report ---")
            for res in results:
                # .get() retrieves the return value of the function
                print(f"   {res.get()}")
                
            total_time = (end_main - start_main).total_seconds()
            print(f"\n   ⏱️  Total Execution Time: {total_time}s")
            
        except Exception as ex:
            print(f"   💥 CRASH: {ex}")

if __name__ == "__main__":
    writer = FastWriter()
    writer.run_pool_demo()
