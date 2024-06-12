# L7_Informatics_assignment_ancy
Git repo for the assignmentround of L7 Informatics

# Ice Cream Shop Application

## Setup

1. Install Python 3.
2. Run the following command to set up the database:

    ```sh
    python setup_db.py
    ```

3. Run the main application:

    ```sh
    python ice_cream_shop.py
    ```

## Usage

1. Follow the menu prompts to add flavors, ingredients, suggestions, allergens, and manage your cart.
2. Search for flavors by season or view all flavors.

## Testing

- Test adding new flavors, ingredients, suggestions, and allergens.
- Test searching for flavors by season.
- Test adding items to the cart and viewing the cart.

## Docker

1. Build the Docker image:

    ```sh
    docker build -t ice_cream_shop .
    ```

2. Run the Docker container:

    ```sh
    docker run -it --rm ice_cream_shop
    ```

3. Follow the menu prompts inside the Docker container to use the application.
