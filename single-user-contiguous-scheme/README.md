# 🗂️ Single User Contiguous Scheme

## 📖 What is it?

The **Single User Contiguous Scheme** is the **simplest memory allocation scheme**, primarily used in the earliest generations of computer systems.  

It is based on three key ideas:  
- **Single** → Only one program can be in memory at a time  
- **Entirety** → A program must be loaded in its entirety before it can run  
- **Contiguous** → The program is allocated one continuous block of memory  

---

## 📝 Characteristics
- Each program is loaded into memory as a whole.  
- The program is allocated as much contiguous space as it needs.  
- If the program is too large to fit into memory, it **cannot run**.  
- Only **one job at a time** is in memory.  

---

## 🖥️ Historical Context
- Common in **early computer systems**.  
- Straightforward to implement.  
- Extremely limited in terms of **multi-tasking** and **resource utilization**.  

---

✅ *This file is part of my OS Algorithms in Python project — where I simulate what I learned in my Operating Systems class.*  
