### Shoe Inventory Program
This Python program is an inventory management system for a shoe store which was created on week 9 of HyperionDev, as part of the solo projects. 

The program uses a Shoe class to represent individual shoes, storing attributes like country, code, product name, cost, and quantity. Users can interact with the shoe inventory through a menu-driven interface, offering the following features:

- Data Management: The program reads shoe data from the inventory.txt file. It creates Shoe objects and stores them in a list, representing the shoe inventory.

- User Interface: The program presents a user-friendly menu where users can choose various options, including:

  - Viewing all available shoes, displayed in a tabulated format.
  - Calculating and displaying the value per item for each shoe.
  - Adding new shoes to the inventory, specifying product name,  cost, and quantity.
  - Searching for a specific shoe by its code.
  - Re-stocking shoes by increasing the quantity of the shoe with the lowest quantity.
  - Tabulated Display: The program uses the tabulate module to present shoe information in a well-organised table format.

- Error Handling: The program handles potential errors, such as file not found or invalid user inputs, providing informative error messages.

- Data Persistence: The program updates the inventory file (inventory.txt) when re-stocking occurs, ensuring data persistence between program runs.





