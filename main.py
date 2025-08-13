from fastapi import FastAPI
"""
---------------------------
fastapi (module)      - The entire installed package
└── FastAPI (class)   - A class definition inside the module
"""

import cowsay 
import math 

"""
MODULES vs. CLASSES in Python:
-------------------------------
- A MODULE (e.g., `math`, `cowsay`) is a .py file containing reusable code:
  * Can contain functions (`math.sqrt()`, `cowsay.cow()`)
  * Can contain constants/objects (`math.pi`)
  * Used directly: `import math` → `math.sqrt(4)`

- A CLASS (e.g., `FastAPI`) is a blueprint for creating objects:
  * Must be instantiated: `app = FastAPI()`
  * Used when you need stateful behavior (tracking routes, configs, etc.)

Key Difference:
  `math` and `cowsay` are modules with ready-to-use tools.
  `FastAPI` is a class inside a module that requires object creation.
"""
#======================================================================



app = FastAPI() #Creates an FastAPI Object

@app.get("/") # This is an .GET http method 
async def root():
    return {"message": "Hello World"}



