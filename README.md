| ID  | Issue Description                        | Identified By | Fixed By     |
|-----|------------------------------------------|---------------|--------------|
| 1   | Style.css is not filled                                    |         Narain |     Whole Team     |
| 2   | in items.py: router was initialized as empty dict                       Pragya               
| 3   | in items.py: duplicate post route for same endpoint was there            Pragya                           
| 4   | in items.py: assuming we want to delete only one item: there were dual delete operations, incorrect path parameters, and was outputting wrong "deleted_item"                                                                       Pragya
| 5   | in users.py: incorrect HTTP method for get_users() - it should obviously be a "get" instead of a "post"  Pragya
| 6   | in users.py: duplicate post route for "/"                               Pragya
| 7   | in users.py: invalid delete function - delete_all() is not a valid function - changed it to delete_one()    Pragya
| 8   | in quiz.py: in get_question(), it always returned the first question, we put a random function to simulate a proper quiz    Prathmesh
| 9   | in quiz.py: HTTP method for submitting answers should be "POST" not "GET"                          Prathmesh
| 10  | in analytics.py: users list had dummy data, removed that and started with a empty list  sambhavi
| 11  | in analytics.py: incorrect field names: item["names"] -> item["name"] & user["usernames"] -> user["username"]   sambhavi
| 12  | in analytics.py: generated histogram image was not being returned in json response sambhavi
| 13  | in models.py: item class was not inheriting from pydantic BaseModel    Prathmesh
| 14  | in models.py: in item class name field should be "str" instead of "int" Prathmessh
| 15  | in main.py: added prefix "/analytics" to analytics_router & "/quiz" to quiz_router   sambhavi
| 16  | in main.py: removed the get_home() function and "/home" API endpoint    sambhavi
| 17   added navigation links in analytics.html      Aishani Sood       Aishani Sood              |               |              |
| 18   | made src empty in analytics.html          Aishani Sood      Aishani Sood               |               |              |
| 19  |       add container in item.html          Aishani Sood     Aishani Sood                    |               |              |
| 20  |analytics.js-sends image as base64 in data.plot_base64  Aishani Sood  Aishani Sood
| 21 | news.js   better error  handling           Sara
|22|  profle.js html code was looking for userCounts Sara
|23| their was of no use PATCH ,we need to use DELETE,    Sara                                 |               |            
 24 | quiz.js...their should be .hidden in styles. Sara    
|25| remove home.js  Sara
 26 | in db.py Standardized collection names to plural     
        # FROM: items_collection: db["item"]                 Prathmesh 