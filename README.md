# XLS to XLSX Converter API

This Python Flask API allows you to upload `.xls` files and converts them to `.xlsx`. It's designed to be used with external services like **Power Automate**.

## API Endpoints

### Convert `.xls` to `.xlsx`
**URL**: `/convert`

**Method**: `POST`

**Parameters**:
- `file`: `.xls` file uploaded as form-data.

**Response**:
- If the conversion is successful, the API will return the converted `.xlsx` file as a download.

## Requirements

- Python 3.x
- Flask
- pandas
- openpyxl

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/xls_to_xlsx_converter.git
    cd xls_to_xlsx_converter
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the API locally:
    ```bash
    python app.py
    ```

The API will start on `http://localhost:5000`.

## Using with Power Automate

To integrate this API with Power Automate:
1. Deploy this API (using a cloud service like Heroku or PythonAnywhere).
2. In Power Automate, use the `HTTP` action to `POST` to your API's `/convert` endpoint.
3. Attach the `.xls` file as form-data in the request.
4. The response will contain the `.xlsx` file, which you can use in subsequent Power Automate steps.

## License

MIT License
