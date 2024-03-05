from flask import Flask, request
import math

app = Flask(__name__)

@app.route("/")
def calculator():
  return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    
    <style>
        input[type=number] {
            width: 400px;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
        ::placeholder{
            color: rgb(113, 109, 109);
            font-size: 15px;
            font-weight: bold;
        }
        input[type=text], select {
            width: 150px;
            padding: 12px 20px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        } 
  
        input[type=submit] {
            width: 400px;
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            align-self: center;
            font-size: 18px;
        }
  
        input[type=submit]:hover {
            background-color: #45a049;
        }
  
        div {
            border-radius: 5px;
            background-color: #f2f2f2;
            padding: 20px;
        }

        label{
          font-size: 25px;
            font-family: Arial, Helvetica, sans-serif;
        }

    </style>
</head>
<body>
    <form action="/calculate" method="post">
        
        <label for="molar_mass">Molar mass of compound:</label>
        <input type="number" id="molar_mass" name="molar_mass" min="0" placeholder=" g/mol">
        
        <br>
        <br>
        <label for="number">Given number:</label>
        <input type="number" id="number" name="number" min="0" placeholder="Given Number...">
        <br>
        <br>
        
        <label for="convert_from">From: </label>
            <select name="unit-from" id="units-from">
                <option value="Particles">Particles</option>
                <option value="mol">mol</option>
                <option value="g">g</option>
            </select>
            
        <label for="convert_to">To: </label>
            <select name="unit-to" id="units-to">
                <option value="Particles">Particles</option>
                <option value="mol">mol</option>
                <option value="g">g</option>
            </select>
        <br>
        <input type="submit" value="Calculate">
    </form>
</body>
</html>'''

@app.route("/calculate",methods=["POST"])
def calculate():
  from_unit = str(request.form['unit-from'])
  to_unit = str(request.form['unit-to'])
  molar_mass = float(request.form['molar_mass'])
  given_number = float(request.form['number'])
  Na = 6.02214076 * (math.pow(10,23))
  answer = 0
  if from_unit == 'g' and to_unit == 'mol':
    answer = given_number * (1/ molar_mass)
    
  elif from_unit == 'mol' and to_unit == 'g':
    answer = given_number * molar_mass
    
  elif from_unit == 'mol' and to_unit == 'Particles':
    answer = given_number * Na
    
  elif from_unit == 'Particles' and to_unit == 'mol':
    answer = given_number * (1/ Na)
    
  elif from_unit == 'g' and to_unit == 'Particles':
    answer = (given_number * (1/ molar_mass)) * Na
    
  elif from_unit == 'Particles' and to_unit == 'g':
    answer = (given_number * (1/ Na)) * molar_mass
  elif from_unit == 'Particles' and to_unit == 'Particles':
    return calculator()
  elif from_unit == 'mol' and to_unit == 'mol':
    return calculator()
  elif from_unit == 'g' and to_unit == 'g':
    return calculator()
  
    
  answer_string = str(answer)
  specific = float(answer_string[:-4])
  rounded = round(specific,2)
  roundd = round(answer,2)

  if answer_string[-4] == "e":
    return f'''
          <h1 style="font-family: Arial, Helvetica, sans-serif;">The answer is:</h1>
          <h2 style="font-family: Arial, Helvetica, sans-serif;">{rounded} x10<sup>{answer_string[-3:]}</sup> {to_unit}</h2>
          <br>
          <a href='./' style="width: 400px; background-color: #4CAF50; color: white; padding: 14px 100px; 
    margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; align-self: center; font-size: 18px;
    text-decoration: none; font-family: Arial, Helvetica, sans-serif;">Go back</a>
'''
  else:
    return f'''<h1 style="font-family: Arial, Helvetica, sans-serif;">The answer is:</h1>
               <h2 style="font-family: Arial, Helvetica, sans-serif;">{roundd}</sup> {to_unit}</h2>
               <br>
               <a href='./' style="width: 400px; background-color: #4CAF50; color: white; padding: 14px 100px; 
    margin: 8px 0; border: none; border-radius: 4px; cursor: pointer; align-self: center; font-size: 18px;
    text-decoration: none; font-family: Arial, Helvetica, sans-serif;">Go back</a>
'''
    
if __name__ == '__main__':
    app.run(port=7007,  debug=True)

