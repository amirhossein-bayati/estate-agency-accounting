# estate-agency-accounting

# Run
First make sure that ms sql server is up! <br />
If you dont have sql sever, make sure use_db="False" is set in '.env' file, then app will connect to sqlite.
```
pip3 install -r requirements.txt
set FLASK_APP='models.py'
cd app
flask db init && flask db migrate && flask db upgrade
```

# Usage
After migrating database run below command for inserting sample records:
```
python gui\main.py
```
username : admin<br/>
password : root<br/><br/>


All of possible queries are in 'queries.py' file in app folder.


# Options
* user login/signup panel
* sqlite3 data base
* add/edit/remove data
* search on data
* multiple contracts


# images
<details>
  <summary>login page</summary>
  <img src="https://github.com/amirhossein-bayati/estate-agency-accounting/blob/main/_screenshots/login_page.png" name="image-name">
</details>
<details>
  <summary>home page</summary>
  <img src="https://github.com/amirhossein-bayati/estate-agency-accounting/blob/main/_screenshots/home_page.png" name="image-name">
</details>
<details>
  <summary>estates page</summary>
  <img src="https://github.com/amirhossein-bayati/estate-agency-accounting/blob/main/_screenshots/estates_page.png" name="image-name">
</details>
<details>
  <summary>customers page</summary>
  <img src="https://github.com/amirhossein-bayati/estate-agency-accounting/blob/main/_screenshots/customers_page.png" name="image-name">
</details>
<details>
  <summary>contracts page</summary>
  <img src="https://github.com/amirhossein-bayati/estate-agency-accounting/blob/main/_screenshots/contracts_page.png" name="image-name">
</details>
<details>
  <summary>employees page</summary>
  <img src="https://github.com/amirhossein-bayati/estate-agency-accounting/blob/main/_screenshots/employee_page.png" name="image-name">
</details>
<details>
  <summary>searching</summary>
  <img src="https://github.com/amirhossein-bayati/estate-agency-accounting/blob/main/_screenshots/search.png" name="image-name">
</details>
