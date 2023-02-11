CREATE DATABASE  IF NOT EXISTS `LELOG`;
USE `LELOG`;

drop table if exists orders;

drop table if exists credit_cards;

drop table if exists recipe_ingredients;

drop table if exists recipe_photos;

drop table if exists recipe_steps;

drop table if exists recipes;

drop table if exists save_for_later;

drop table if exists articles;

drop table if exists searches;

drop table if exists wish_lists;

drop table if exists customers;

drop table if exists products;


-- Host: localhost    Database: LELOG
-- ------------------------------------------------------
-- Server version	8.0.20

# /*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
# /*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
# /*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
# /*!50503 SET NAMES utf8 */;
# /*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
# /*!40103 SET TIME_ZONE='+00:00' */;
# /*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
# /*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
# /*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
# /*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `Article_ID` int NOT NULL,
  `Author_Name` varchar(50) NOT NULL,
  `Article_Name` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  `Content` longtext NOT NULL,
  `Reading_Time` int DEFAULT NULL,
  PRIMARY KEY (`Article_ID`)
);

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` VALUES (1,'Mr. Ipsum Loren','Cooking at Home','cooking at home.jpg','Whether you live on your own or are a busy parent, finding the time and energy to prepare home-cooked meals can seem like a daunting task. At the end of a hectic day, eating out or ordering in might feel like the quickest, easiest option. But convenience and processed food can take a significant toll on your mood and health.\n\nConvenience food is typically high in chemical additives, hormones, sugar, salt, unhealthy fat, and calories, all of which can adversely affect your brain and outlook. It can leave you feeling tired, bloated, and irritable, and exacerbate symptoms of depression, stress, and anxiety.\n\nRestaurants often serve more food than you should eat. Many restaurants serve portions that are two to three times larger than the recommended dietary guidelines. This encourages you to eat more than you would at home, adversely affecting your waistline, blood pressure, and risk of diabetes.\n\nWhen you prepare your own meals, you have more control over the ingredients. By cooking for yourself, you can ensure that you and your family eat fresh, wholesome meals. This can help you to look and feel healthier, boost your energy, stabilize your weight and mood, and improve your sleep and resilience to stress.\n\nCooking at home doesn’t have to be complicated. The cornerstone of a healthy diet is to eat food that is as close as possible to the way nature made it. That means replacing processed food with real food whenever possible and eating plenty of vegetables and healthy sources of protein. It doesn’t mean you have to spend hours in the kitchen combining hundreds of different ingredients or slavishly following elaborate recipes. In fact, simple meals are often the tastiest.\n\nCooking at home can even take less time that eating out. There are plenty of quick, simple, and wholesome meals you can cook at home in less time than it takes to travel to a restaurant or wait for a delivery.\n\nCooking at home is also a great way to spend time with others—and you don’t have to be an accomplished chef. Whatever your abilities or experience as a cook, you can learn to prepare quick and healthy meals that can have real benefits for your mental and physical health.\n\n',13),(2,'Asaf Sharf','What It Takes to Build the Unbeatable Body','bodybuild.jpg','Can I break a record?\"\n\n\"Why not?\" replies Bill Kaiser, an aquatics specialist for USA Swimming. He snaps a harness around my midsection. I slip into lane one of the 50-meter (164-foot) pool at the Olympic Training Center in Colorado Springs, nod to Kaiser, and shove off the wall.\n\nSuddenly my body feels like a bullet ripping through the water. Never have my arms and shoulders rotated with such power. Each stroke seems to propel me twice the usual distance. I feel instantly euphoric, as if my brain were surging with endorphins.\n\nKaiser has hooked my harness to a pulley system known as a tow, a training device that drags a high-performance swimmer 5 percent faster than he usually swims. It allows the swimmer to get a feel for the increased speed, adjust his stroke patterns and body rotations accordingly, and eventually swim faster on his own. In my case, the tow is moving almost 50 percent faster than my norm.\n\n\"Twenty-three seconds later I touch the wall. \"Congratulations,\" says Kaiser. \"Youve just beaten Amy Van Dykens American record for the 50 free.\"\n\nHe is referring to the 50-meter freestyle race Van Dyken swam in 24.87 seconds in the 1996 Olympics in Atlanta. With that and three other events she became the first American woman to win four gold medals in one Olympics.\n\nI am not an Olympic-caliber competitor. I am a middle-age masters swimmer who has won a few medals in my age group.\n\nThe human body, I know, did not evolve to swim laps—or to kick a soccer ball or to do somersaults off a 10-meter (33-foot) platform. But as long as humans have had a sense of sport and competition, we have invented ways to push our anatomy to its limits. What are those limits? In this Olympic year I am studying some of the men and women trained to perform as if there were none.\n\nNumerous factors—genetic, psychological, cultural, and financial—go into making a super performer, but the right genes may be the most critical. Elite athletes, as these super performers are called, are in a sense fortunate freaks of nature\n\n',53),(3,'Dr. Prof. Patrick','A History of Pizza','pizza.png','Pizza is the world’s favourite fast food. We eat it everywhere – at home, in restaurants, on street corners. Some three billion pizzas are sold each year in the United States alone, an average of 46 slices per person. But the story of how the humble pizza came to enjoy such global dominance reveals much about the history of migration, economics and technological change.\n\nPeople have been eating pizza, in one form or another, for centuries. As far back as antiquity, pieces of flatbread, topped with savouries, served as a simple and tasty meal for those who could not afford plates, or who were on the go. These early pizzas appear in Virgil’s Aeneid. Shortly after arriving in Latium, Aeneas and his crew sat down beneath a tree and laid out ‘thin wheaten cakes as platters for their meal’. They then scattered them with mushrooms and herbs they had found in the woods and guzzled them down, crust and all, prompting Aeneas’ son Ascanius to exclaim: “Look! We’ve even eaten our plates!”\n\nBut it was in late 18th-century Naples that the pizza as we now know it came into being. Under the Bourbon kings, Naples had become one of the largest cities in Europe – and it was growing fast. Fuelled by overseas trade and a steady influx of peasants from the countryside, its population ballooned from 200,000 in 1700 to 399,000 in 1748. As the urban economy struggled to keep pace, an ever greater number of the city’s inhabitants fell into poverty. The most abject of these were known as lazzaroni, because their ragged appearance resembled that of Lazarus. Numbering around 50,000 they scraped by on the pittance they earned as porters, messengers or casual labourers. Always rushing about in search of work, they needed food that was cheap and easy to eat. Pizzas met this need.\n\nSold not in shops, but by street vendors carrying huge boxes under their arms, they would be cut to meet the customer’s budget or appetite. As Alexandre Dumas noted in Le Corricolo (1843), a two liard slice would make a good breakfast, while two sous would buy a pizza large enough for a whole family. None of them were terribly complicated. Though similar in some respects to Virgil’s flatbreads, they were now defined by inexpensive, easy-to-find ingredients with plenty of flavour. The simplest were topped with nothing more than garlic, lard and salt. But others included caciocavallo (a cheese made from horse’s milk), cecenielli (whitebait) or basil. Some even had tomatoes on top.\n\nOnly recently introduced from the Americas, these were still a curiosity, looked down upon by contemporary gourmets. But it was their unpopularity – and hence their low price – that made them attractive.\n',45),(4,'Mrs. Puff','Ditch the Gluten, Improve Your Health?','health without gluten.jpg','This just in: A new health myth has been taking the country by storm.\n\nPerhaps I anexaggerating a bit. After all, health fads— especially diet fads— have come and gone for decades. Some are more worthy than others. For example, I am impressed by the evidence supporting the Mediterranean diet as a healthy option. As each one of us is different, the \"ideal diet\" may not be the same for each person. But the interest and enthusiasm surrounding the gluten-free food movement in recent years has been remarkable. Not so long ago, relatively few people had ever heard of gluten. And it certainly was not the \"food movement\" it has recently become.\n\nIf you are considering limiting your consumption of gluten, you are certainly not alone. But the question is: Will restricting the gluten you eat improve your health? And will it make you feel better? It is appealing to think so.\n\nGluten is a protein found in many grains, including wheat, barley and rye. It is common in foods such as bread, pasta, pizza and cereal. Gluten provides no essential nutrients. People with celiac disease have an immune reaction that is triggered by eating gluten. They develop inflammation and damage in their intestinal tracts and other parts of the body when they eat foods containing gluten. Current estimates suggest that up to 1% of the population has this condition. A gluten-free diet is necessary to eliminate the inflammation, as well as the symptoms.\n\nGrocery stores and restaurants now offer gluten-free options that rival conventional foods in taste and quality; in years past, it was much harder to maintain a gluten-free diet.\n',5),(5,'Omer Ries','How much water should you drink?','water.jpg','How much water should you drink a day? You probably know that it is important to drink plenty of fluids when the temperatures soar outside. But staying hydrated is a daily necessity, no matter what the thermometer says. Unfortunately, many of us are not getting enough to drink, especially older adults.\n\n\"Older people dont sense thirst as much as they did when they were younger. And that could be a problem if they are on a medication that may cause fluid loss, such as a diuretic,\" says Dr. Julian Seifter, a kidney specialist and associate professor of medicine at Harvard Medical School.\n\nGiving your body enough fluids to carry out those tasks means that you are staying hydrated.\n\nIf you dont drink enough water each day, you risk becoming dehydrated. Warning signs of dehydration include weakness, low blood pressure, dizziness, confusion, or urine that is dark in color.\n\nSo how much water should you drink? Most people need about four to six cups of water each day.\n\nThe daily four-to-six cup rule is for generally healthy people. It is possible to take in too much water if you have certain health conditions, such as thyroid disease or kidney, liver, or heart problems; or if you are taking medications that make you retain water, such as non-steroidal anti-inflammatory drugs (NSAIDs), opiate pain medications, and some antidepressants.\n',15),(6,'Amit Powitzer','Celiac disease: From pathophysiology to treatment','celiac.jpg','Celiac disease, also known as “celiac sprue”, is a chronic inflammatory disorder of the small intestine, produced by the ingestion of dietary gluten products in susceptible people.\n\nIt is a multifactorial disease, including genetic and environmental factors. Environmental trigger is represented by gluten while the genetic predisposition has been identified in the major histocompatibility complex region. Celiac disease is not a rare disorder like previously thought, with a global prevalence around 1%.\n\nThe reason of its under-recognition is mainly referable to the fact that about half of affected people do not have the classic gastrointestinal symptoms, but they present nonspecific manifestations of nutritional deficiency or have no symptoms at all. Here we review the most recent data concerning epidemiology, pathogenesis, clinical presentation, available diagnostic tests and therapeutic management of celiac disease.\n\nCeliac disease defined an autoimmune disorder originating by an aberrant adaptive immune response against gluten-containing grains in susceptible individuals. Celiac disease was first described in 1888 by Samuel Gee, but only in 1953 it became clear the importance of the gluten in the origin of this pathology. In celiac subjects the ingestion of gluten leads to an enteropathy with an impairment of the mucosal surface and, consequently, abnormal absorption of nutrients.\n\nCeliac disease might be considered a syndrome, because of the wide spectrum of clinical manifestations and the involvement of various human systems. Celiac disease shows peculiar features in comparison to others autoimmune disorders, including the complete recovery of the mucosal damage as well as the reversibility of its progression and chronic dynamics, with a total avoidance of gluten. Conversely, it is now ascertained that undiagnosed celiac disease, might have severe consequences in children as well as in adult subjects.\n\nBesides celiac disease and wheat allergy, a new entity has been included, apparently not driven by an immune response: The non-celiac gluten sensitivity (NCGS). The pathogenesis of NCGS remains largely unknown, although it is now ascertained that it includes a set of factors[3,11]. Here, we review the epidemiology, pathogenesis, clinical presentation, diagnostic tests and therapeutic management of celiac disease.\n',55);

--
-- Table structure for table `customers`
--

CREATE TABLE `customers` (
  `Customer_ID` int NOT NULL,
  `Register_Date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Email` varchar(30) DEFAULT NULL,
  `Password` varchar(16) NOT NULL,
  `First_Name` varchar(10) NOT NULL,
  `Last_Name` varchar(10) NOT NULL,
  `Phone_Number` varchar(15) DEFAULT NULL,
  `username` varchar(30) NOT NULL,
  PRIMARY KEY (`Customer_ID`),
  CONSTRAINT `C_Email` CHECK ((`Email` like _utf8mb4'%@%.%'))
);

--
-- Dumping data for table `customers`
--

INSERT INTO `customers` VALUES (1,'2020-05-05 00:00:00','awdl@gerg.com','qwe','noa','wasserman','0503069922','waser'),(2,'2020-01-01 00:00:00','nitaymayo@gmail.com','nitay111','Nitay','Mayo','050-9065533','nitay'),(3,'2019-03-03 00:00:00','nitaymayo@gmail.com','nitay111','Nitay','Mayo','050-9065533','pow'),(4,'2018-06-08 00:00:00','email@gerg.com','new password','first','last','phone','bensha'),(5,'2019-10-05 00:00:00','omerries@gmail.com','or987654321','Omer','Ries','050-5489027','ries'),(6,'2019-03-08 00:00:00','erelsimani@gmail.com','erelsi123','Erel','Simani','050-998234','sima'),(7,'2020-07-08 04:10:43','qwe@fwed.com','qwe','qwe','qwe','05060099995','qwe'),(8,'2020-07-08 15:52:37','sfsf@dfbfs.wrwr','123','sfb','sfb','fbrwb','vbsf'),(9,'2020-07-08 15:53:45','sfsf@dfbfs.wrwr','123','sfb','sfb','fbrwb','vbsf'),(10,'2020-07-08 20:48:34','ni@sj.com','123','sharf','shar','050306606','sharf'),(11,'2020-07-08 21:21:03','qwe@gmail.com','qwe','qwe','qwe','050306002','qwe'),(12,'2020-07-09 01:52:52','un@jnawd.com','123','rozen','rosen','654465456456','rosen');


--
-- Table structure for table `credit_cards`
--

CREATE TABLE `credit_cards` (
  `Customer_ID` int NOT NULL,
  `Card_Number` varchar(16) NOT NULL,
  `CVV` char(3) NOT NULL,
  `Exp_Date` date NOT NULL,
  `Type` varchar(20) NOT NULL,
  PRIMARY KEY (`Customer_ID`,`Card_Number`),
  CONSTRAINT `fk_C_Card` FOREIGN KEY (`Customer_ID`) REFERENCES `customers` (`Customer_ID`)
);


--
-- Dumping data for table `credit_cards`
--

INSERT INTO `credit_cards` VALUES (1,'1234123412341234','123','2024-01-01','visa'),(2,'1234567812345678','455','2025-01-04','isracard'),(3,'5555444433332222','789','2022-02-01','visa'),(4,'1111876522225678','114','2024-10-05','visa'),(5,'1111222233334444','105','2024-12-01','visa'),(6,'8765876587658765','983','2026-10-03','isracard');

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `Product_ID` int NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Price` int NOT NULL,
  `Image` varchar(500) NOT NULL,
  `Description` varchar(500) NOT NULL,
  `Contain` varchar(500) NOT NULL,
  `May_Contain` varchar(500) NOT NULL,
  `Nutritional_Values` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Product_ID`)
);

--
-- Dumping data for table `products`
--

INSERT INTO `products` VALUES (111,'Pizza',30,'pizza.png','Classic homemade pizza, made with best materials','soy, milk','nuts','100 gr calories, 99 gr fat, 10 gr suger, 87 gr carbs'),(112,'Quaker',20,'Quaker.png','A hearty hot bowl of Quaker Old Fashioned Oats','soy','milk powder','100 gr calories, 99 gr fat, 10 gr suger, 87 gr carbs'),(122,'Cookies',24,'Cookies.png','A simple, amazingly delicious, doughy yet still fully cooked, chocolate chip cookie','almonds, cacao, milk powder','nuts','100 gr calories, 99 gr fat, 10 gr suger, 87 gr carbs'),(123,'Bread',14,'bread11.jpg','Homemade white bread, baked up deliciously golden brown','almonds, nuts','fosfat','100 gr calories, 99 gr fat, 10 gr suger, 87 gr carbs'),(134,'Pasta',26,'pasta1.jpg','Delicious pasta dish from classic spaghetti Bolognese','soy, fosfat, nuts','none','100 gr calories, 99 gr fat, 10 gr suger, 87 gr carbs'),(145,'Cake',32,'cake.jpg','The simplest, great tasting choclate cake','milk, cacao','almonds, nuts','100 gr calories, 99 gr fat, 10 gr suger, 87 gr carbs');


--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `Order_ID` int NOT NULL,
  `Card_Number` varchar(16) NOT NULL,
  `DT` datetime NOT NULL,
  `Customer_ID` int NOT NULL,
  `Product_ID` int NOT NULL,
  PRIMARY KEY (`Order_ID`),
  KEY `fk_O_C_Num` (`Customer_ID`,`Card_Number`),
  KEY `fk_O_P_ID` (`Product_ID`),
  CONSTRAINT `fk_O_C_Num` FOREIGN KEY (`Customer_ID`, `Card_Number`) REFERENCES `credit_cards` (`Customer_ID`, `Card_Number`),
  CONSTRAINT `fk_O_P_ID` FOREIGN KEY (`Product_ID`) REFERENCES `products` (`Product_ID`)
);

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` VALUES (1112,'1234123412341234','2020-05-05 00:00:00',1,122),(1122,'1234567812345678','2020-07-02 00:00:00',2,122),(1134,'5555444433332222','2019-10-01 00:00:00',3,134),(1142,'1234123412341234','2020-12-03 00:00:00',1,145),(1234,'1234123412341234','2020-05-06 00:00:00',1,111),(2113,'1111876522225678','2019-09-09 00:00:00',4,112),(2142,'1111222233334444','2019-09-12 00:00:00',5,123),(2211,'5555444433332222','2020-04-16 00:00:00',3,123);

--
-- Table structure for table `recipes`
--

CREATE TABLE `recipes` (
  `Recipe_ID` int NOT NULL,
  `Recipe_Name` varchar(50) NOT NULL,
  `Main_Image` varchar(100) NOT NULL,
  `Description` longtext NOT NULL,
  `Nutrition_Info` varchar(500) DEFAULT NULL,
  `Preparation_Time` int DEFAULT NULL,
  `Cooking_Time` int DEFAULT NULL,
  `Additional_Time` int DEFAULT NULL,
  `Servings` int DEFAULT NULL,
  PRIMARY KEY (`Recipe_ID`)
);

--
-- Dumping data for table `recipes`
--

INSERT INTO `recipes` VALUES (1,'Bread','recepieBread.png','Simple gluten-free bread with very rich taste. Thanks to this easy recipe, even if you’re gluten intolerant, you’ll never have to go without again.','102.1 calories, \n	 3.9 g protein, \n     2.1 g carbohydrates, \n     114.4 mg cholesterol, \n     185.7 mg sodium',10,10,40,10),(2,'Pizza','recepiePizza1.png','Stone oven pizza, easy to make. The good-old homemade pizza, perfect for children! You can also add special toppings such as olives, onion, pineapple and more.','137 calories, \n	3.2 g protein, \n	23.1 g carbohydrates, \n	3.7 g fat, \n	2.9 g sugars',15,40,10,8),(3,'Egg Sandwitch','recepieEggSandwich.png','Southern egg salad, primarily used for sandwiches. Serve on fresh bread of your choice. My wife likes to make double-decker sandwiches (utilizing whole Gluten Free bread for the center slice) with pimento cheese on the other half. Trim the edges and cut into 2 or 3 pieces. Great for tailgating','650 calories, \n	8.2 g protein, \n	7.8 g carbohydrates, \n	215.3 mg cholesterol, \n	180.7 mg sodium',10,30,30,10);


--
-- Table structure for table `recipe_ingredients`
--

CREATE TABLE `recipe_ingredients`
(
    `Recipe_ID`  int         NOT NULL,
    `Ingredient` varchar(50) NOT NULL,
    PRIMARY KEY (`Recipe_ID`, `Ingredient`),
    CONSTRAINT `fk_r_ingr` FOREIGN KEY (`Recipe_ID`) REFERENCES `recipes` (`Recipe_ID`)
);

--
-- Dumping data for table `recipe_ingredients`
--

INSERT INTO `recipe_ingredients` VALUES (1,'½ teaspoon sea salt'),(1,'2 large eggs'),(1,'2 tablespoons golden caster sugar'),(1,'3 tablespoons olive oil'),(1,'325 ml semi-skimmed milk'),(1,'450 g gluten-free brown bread flour'),(2,'2 cups pizza-base'),(2,'2 teaspoons salt'),(2,'200 grams mushrooms'),(2,'400 grams tomatoes'),(2,'5 cups water'),(2,'500 grams cheese'),(2,'6 large eggs'),(3,'1 teaspoon lemon juice'),(3,'1 teaspoon white sugar'),(3,'⅓ cup mayonnaise'),(3,'2 tablespoons salt'),(3,'2 teaspoons yellow mustard'),(3,'6 large eggs');

--
-- Table structure for table `recipe_photos`
--

CREATE TABLE `recipe_photos` (
  `Recipe_ID` int NOT NULL,
  `Photo_Link` varchar(50) NOT NULL,
  PRIMARY KEY (`Recipe_ID`,`Photo_Link`),
  CONSTRAINT `fk_Recipe_Photo` FOREIGN KEY (`Recipe_ID`) REFERENCES `recipes` (`Recipe_ID`)
);

--
-- Dumping data for table `recipe_photos`
--

INSERT INTO `recipe_photos` VALUES (1,'recepieBread2.png'),(1,'recepieBread3.png'),(1,'recepieBread4.png'),(1,'recepieBread5.png'),(1,'recepieBread6.png'),(2,'recepiePizza2.png'),(2,'recepiePizza3.png'),(2,'recepiePizza4.png'),(2,'recepiePizza5.png'),(2,'recepiePizza6.png'),(3,'recepieEggSandwich2.png'),(3,'recepieEggSandwich3.png'),(3,'recepieEggSandwich4.png'),(3,'recepieEggSandwich5.png'),(3,'recepieEggSandwich6.png');

--
-- Table structure for table `recipe_steps`
--

CREATE TABLE `recipe_steps` (
  `Recipe_ID` int NOT NULL,
  `Step_Num` int NOT NULL,
  `Content` longtext NOT NULL,
  PRIMARY KEY (`Recipe_ID`,`Step_Num`),
  CONSTRAINT `fk_r_step` FOREIGN KEY (`Recipe_ID`) REFERENCES `recipes` (`Recipe_ID`)
);

--
-- Dumping data for table `recipe_steps`
--

INSERT INTO `recipe_steps` VALUES (1,1,'Preheat the oven to 200ºC/400ºF/gas 6. Warm the milk in a small pan over a low heat, then leave to cool slightly.\n	Crack the eggs into a large bowl, add the vinegar, then gradually stir in the warm milk until combined.'),(1,2,'Combine the flour, salt, sugar and yeast in another bowl, then, using a wooden spoon, stir the dry ingredients\n	into the wet mixture until it forms a sticky dough. Add the olive oil, then bring it together with your hands into a ball,'),(1,3,'Place onto a lightly oiled baking tray, cover with a damp tea towel,\n	then leave to prove in a warm place for around 1 hour, or until doubled in size. Once risen, place the tray in the hot oven and bake\n	for around 35 minutes, or until golden and cooked through. '),(2,1,'Place the warm water in the large bowl of a heavy duty stand mixer.\n    Sprinkle the yeast over the warm water and let it sit for 5 minutes until the yeast is dissolved.'),(2,2,'Using the mixing paddle attachment, mix in the flour, salt, sugar, and\n    olive oil on low speed for a minute. Then replace the mixing paddle with the dough hook attachment.'),(2,3,'Knead the pizza dough on low to medium speed using the dough hook about 7-10 minutes.\n    if you dont have a mixer, you can mix the ingredients together and knead them by hand.'),(3,1,'Cover eggs with water in a saucepan, bring to a low boil, let boil slowly for 5 minutes.\n    Remove from heat and let stand, covered, for 5 minutes.'),(3,2,'Transfer eggs to ice water to chill for 5 minutes; peel. Grate eggs into a\n    medium mixing bowl and add mayonnaise, relish, mustard, sugar, lemon juice, salt, pepper, and hot sauce. Mix well.'),(3,3,'Chill in the refrigerator for at least 30 minutes.');

--
-- Table structure for table `save_for_later`
--

CREATE TABLE `save_for_later` (
  `Customer_ID` int NOT NULL,
  `Article_ID` int NOT NULL,
  PRIMARY KEY (`Customer_ID`,`Article_ID`),
  KEY `fk_ARTICLES_ID` (`Article_ID`),
  CONSTRAINT `fk_ARTICLES_ID` FOREIGN KEY (`Article_ID`) REFERENCES `articles` (`Article_ID`),
  CONSTRAINT `fk_CUSTOMER_ID` FOREIGN KEY (`Customer_ID`) REFERENCES `customers` (`Customer_ID`)
);

--
-- Table structure for table `searches`
--

CREATE TABLE `searches` (
  `Customer_ID` int NOT NULL,
  `DT` datetime NOT NULL,
  `Content` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`Customer_ID`,`DT`),
  CONSTRAINT `fk_C_ID_Search` FOREIGN KEY (`Customer_ID`) REFERENCES `customers` (`Customer_ID`)
);

--
-- Dumping data for table `searches`
--

INSERT INTO `searches` VALUES (1,'2020-05-05 00:00:00','pasta'),(1,'2020-07-03 00:00:00','payment policy'),(2,'2020-01-08 00:00:00','meat balls recipe'),(3,'2019-12-05 00:00:00','sign up form'),(4,'2019-01-01 00:00:00','pasta'),(4,'2020-02-03 00:00:00','whole bread'),(4,'2020-07-05 00:00:00','pasta recipe'),(5,'2020-05-06 00:00:00','payment');

--
-- Table structure for table `wish_lists`
--

CREATE TABLE `wish_lists` (
  `Customer_ID` int NOT NULL,
  `Product_ID` int NOT NULL,
  PRIMARY KEY (`Customer_ID`,`Product_ID`),
  KEY `fk_P_ID` (`Product_ID`),
  CONSTRAINT `fk_C_ID` FOREIGN KEY (`Customer_ID`) REFERENCES `customers` (`Customer_ID`),
  CONSTRAINT `fk_P_ID` FOREIGN KEY (`Product_ID`) REFERENCES `products` (`Product_ID`)
);

--
-- Dumping data for table `wish_lists`
--

INSERT INTO `wish_lists` VALUES (12,111),(12,112),(12,122);

