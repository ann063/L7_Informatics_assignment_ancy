# L7_Informatics_assignment_ancy
Git repo for the assignment round of L7 Informatics

## NAME- ANCY SHARMILA D
## REG NO- 20MIS0211

# Ice Cream Parlor Application


Overview
This Python application manages an ice cream parlor cafe using SQLite for database management. It allows users to handle seasonal flavor offerings, ingredient inventory, customer flavor suggestions, and allergy concerns. Users can maintain a cart of their favorite products, search and filter offerings, and add allergens if they don’t already exist.

Features
	1.	Manage Seasonal Flavors: Add and view seasonal flavors.
	2.	Ingredient Inventory: Add and manage ingredients.
	3.	Customer Suggestions: Add customer flavor suggestions.
	4.	Allergy Concerns: Add and manage allergens.
	5.	Customer Cart: Add flavors to a customer cart.
	6.	Search & Filter: Search and filter seasonal flavors.
	7.	Docker Support: Build and run the application in a Docker container.

Initial Setup
1.	Clone the Repository:
git clone <https://github.com/ann063/L7_Informatics_assignment_ancy.git>
cd ice_cream_parlor

2.	Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows use `.\venv\Scripts\activate`

3.	Install Dependencies:
pip install -r requirements.txt

4.	Setup the Database:
python app/setup_db.py

5.	Run the Application:
python app/ice_cream_shop.py

Docker Setup
1.	Build the Docker Image:
docker build -t ice_cream_shop app/.

2.	Run the Docker Container:
docker run -it --rm ice_cream_shop


4. Output Screenshots
<img width="350" alt="image" src="https://github.com/ann063/L7_Informatics_assignment_ancy/assets/116182515/1ab66260-3dfb-41ab-a4f7-e7ef9f0a64d7">
<img width="350" alt="image" src="https://github.com/ann063/L7_Informatics_assignment_ancy/assets/116182515/a48e13e8-6121-4878-916d-57f6d1d05ca1">
<img width="239" alt="image" src="https://github.com/ann063/L7_Informatics_assignment_ancy/assets/116182515/d5c800be-d2cc-4161-bd51-d10c7c488c73">
<img width="239" alt="image" src="https://github.com/ann063/L7_Informatics_assignment_ancy/assets/116182515/56948a2e-a83a-43e2-b3ce-0405b046f5cd">
<img width="239" alt="image" src="https://github.com/ann063/L7_Informatics_assignment_ancy/assets/116182515/4c23567e-d278-44cb-93b0-0c99b49ec060">
<img width="372" alt="image" src="https://github.com/ann063/L7_Informatics_assignment_ancy/assets/116182515/44f485d5-3808-47b5-a167-e0d25a139872">
<img width="271" alt="image" src="https://github.com/ann063/L7_Informatics_assignment_ancy/assets/116182515/4dfc03ba-d5ae-459b-bbf0-f91a8454b7c7">
<img width="271" alt="image" src="https://github.com/ann063/L7_Informatics_assignment_ancy/assets/116182515/857183c8-3062-4e7d-a4f5-7cf3aec4a0bc">








