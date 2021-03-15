DROP TABLE `user_hot_dog` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `user_id` TEXT NOT NULL,
    `hot_dog_id` TEXT NOT NULL,
    `date_complete` CURRENT_DATE,
    `is_favorite` BOOLEAN,
    `note` TEXT NOT NULL,
    `is_approved` BOOLEAN
) CREATE TABLE `hot_dog` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `toppings` TEXT NOT NULL,
    `image` TEXT NOT NULL
)