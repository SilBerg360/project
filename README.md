# FijndBrein
#### Video Demo:  <URL https://youtu.be/J0TceZAWJnI>
#### Description: 
---

## 1. Overview
For many psychology students, instantly recalling which brain part does what can be challenging. **FijndBrein** was created to make that process easier. It’s a web app that serves as a brain encyclopedia: you can quickly look up any part of the brain and see an overview of its main functions, how it collaborates with other regions, a clear image of its location, and even a fun nickname to make memorization more intuitive.

---

## 2. Features
The user interface is designed to look calm and simplistic, making it easy to navigate and focus on the content. When searching for a brain part, a dynamic form button is generated using JavaScript, helping to prevent misspellings and ensuring that users can always find the intended region. This works by fetching data from a `/search` route that, with the help of SQLAlchemy, returns all brain part names containing letters in common with the input.

Clicking one of these buttons calls the `/fijnd` route, which retrieves the requested brain part and displays a template with the region name at the top, the nickname below it, and the relevant information presented in an article-style format to make learning more engaging and visually clear.

---

## 3. Files

- **`app.py`** – Handles the backend logic, including routing and interaction with the `brein.db` database via SQLAlchemy. It fetches data for the templates and manages user requests.  

- **`brein.db`** – Stores text elements for each brain part and paths to their images. This database provides the necessary information for `app.py` to generate dynamic HTML pages when a user clicks on a brain part.  

- **`requirements.txt`** – Lists all Python libraries required for FijndBrein to function properly.  

- **`templates/`** – Contains HTML files used by the app:  
  - `layout.html` – Base template used with Jinja in other templates.  
  - `index.html` – Homepage with the search interface.  
  - `fijnd.html` – Displays all information about a selected brain part, dynamically generated using Jinja syntax.  
  - `error.html` – Shows an error message if a user somehow triggers a null response from the database.  

- **`static/`** – Contains supporting assets:  
  - `images/` – Images of all brain parts.  
  - `favicon.ico` – Brain emoji displayed in the browser tab.  
  - `FijndBrein.svg` – Fun illustration on the homepage.  
  - `styles.css` – CSS file for styling the pages and creating the sleek UI.  

---

## 4. Design Choices
One of the most significant decisions was to implement a **local database** instead of using an open-source brain API. The primary goal of FijndBrein is to provide all necessary information in short, easy-to-grasp sentences with digestible images. There isn’t any existing API specifically designed for this purpose, so using a local database was the simplest and most effective solution.

Another key decision was to **exclude a full catalog of all brain parts**. While initially planned, including a catalog could have introduced unnecessary distractions. Since the app is intended as a focused study tool, students only need to search for brain parts they are actively learning. Misspellings are handled gracefully through the dynamic button interface, so the search remains simple and efficient without overwhelming users with extra content.

---

## 5. Challenges & Solutions
One of the first major challenges in developing FijndBrein was handling **brain part lookups**. Brain names can be difficult to type correctly, and even a single-letter typo could previously result in no results or an error. To address this, the dynamic button interface was introduced, using JavaScript and the database’s `LIKE()` search function. This approach displays exactly the available brain parts while forgiving minor misspellings, ensuring a smooth user experience.

Another challenge was creating a **visually appealing interface** without introducing distractions. By strategically using vector images, the UI remains clean and simple while still being engaging. This balance allows users to focus on learning the content without feeling overwhelmed by the visuals.

---

## 6. Future Improvements
A feature that could add significant value for students at the University of Amsterdam is a **translation function**. This would provide clear, well-formulated explanations of each brain area in the primary languages spoken by most students, such as German, Dutch, and French. By allowing users to access content in their mother tongue, the app could become even more accessible and effective as a study tool, helping students understand complex concepts more quickly and accurately.

---

## 7. Conclusion
All in all, I am extremely grateful for the process of creating this web app, even during the many times I almost lost it due to overwriting CSS. This project has shown me that if you persistently tackle a problem, eventually it will yield a solution. Thanks to CS50x for having me (not that they had a choice!), and good luck to all the students using this tool, you make this project worthwhile! ❤️