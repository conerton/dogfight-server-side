DROP TABLE `user_hot_dog` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `user_id` TEXT NOT NULL,
    `hot_dog_id` TEXT NOT NULL,
    `date_complete` CURRENT_DATE,
    `is_favorite` BOOLEAN,
    `note` TEXT NOT NULL,
    `is_approved` BOOLEAN
    INSERT INTO dogfightapi_hotdog (id, name, toppings, image)
    VALUES (
            id :integer,
            'name:varchar(50)',
            'toppings:varchar(500)',
            'image:varchar(10)'
        );
) CREATE TABLE `hot_dog` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `toppings` TEXT NOT NULL,
    `image` TEXT NOT NULL
);
SELECT "dogfightapi_userhotdog"."id",
    "dogfightapi_userhotdog"."user_id",
    "dogfightapi_userhotdog"."hot_dog_id",
    "dogfightapi_userhotdog"."date_completed",
    "dogfightapi_userhotdog"."is_favorite",
    "dogfightapi_userhotdog"."note",
    "dogfightapi_userhotdog"."is_approved"
FROM "dogfightapi_userhotdog"
WHERE "dogfightapi_userhotdog"."user_id" = 1