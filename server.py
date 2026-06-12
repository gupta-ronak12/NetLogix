import pandas as pd
import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse
import os
from classifier_engine import classify

# Initialize FastAPI app
app = FastAPI()

@app.post("/classify/")
async def classify_logs(file: UploadFile):
    # Ensure the uploaded file is a CSV
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV.")
    
    try:
        # Read the uploaded CSV
        df = pd.read_csv(file.file)
        
        # Validate columns
        if "source" not in df.columns or "log_message" not in df.columns:
            raise HTTPException(status_code=400, detail="CSV must contain 'source' and 'log_message' columns.")

        # Perform classification using your engine
        # We pass a list of tuples as expected by your engine
        log_data = list(zip(df["source"], df["log_message"]))
        df["target_label"] = classify(log_data)

        # Save the modified file to the resources folder
        output_dir = "resources"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        output_file = os.path.join(output_dir, "output.csv")
        df.to_csv(output_file, index=False)
        
        print(f"File successfully classified and saved to {output_file}")
        
        # Return the file as a response
        return FileResponse(output_file, media_type='text/csv', filename="classified_logs.csv")

    except Exception as e:
        # Log the error and raise an HTTP exception
        print(f"Error during classification: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        file.file.close()

# This is the "Server Startup" code that keeps the server alive
if __name__ == "__main__":
    print("Starting the Netlogix Log Classification Server...")
    uvicorn.run(app, host="127.0.0.1", port=8000)