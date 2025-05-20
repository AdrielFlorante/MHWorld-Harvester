# Monster Hunter: World - Botanical Research Cultivation Assistant

This application helps you calculate the optimal farming methods for botanical research and cultivation in *Monster Hunter: World*. Utilize this tool to maximize your resource gathering and enhance your hunting experience.

---

## 🌱 Overview of Botanical Research

In *Monster Hunter: World*, botanical research and cultivation are key components for gathering valuable items that assist during hunts.

### Botanical Research Center
- **Function**: Cultivate various items like herbs, mushrooms, and insects after unlocking the center through progression.
- **Rules**: You can cultivate **three different crops at a time**, but only **one fertilizer can be applied per cycle** using Research Points.
  - Each fertilizer has different **effects**, **durations**, and **costs**, and they interact with crops in unique ways.
  - **One cycle** is the duration of finishing **one quest**.

### Research Points
- Earned through quests, gathering, and general gameplay.
- Spent on applying fertilizers to enhance crop efficiency.

### Growing Items
- Choose the items to grow — each has a unique maturation time.
- Fertilizers can **reduce growth time**, **increase yield**, or **extend effect durations**.

### Harvesting
- Once matured, crops are harvested and used for crafting or field use.
- Efficient farming minimizes downtime between harvests.

---

## ❓ The Problem

- There are **countless combinations** of fertilizers and crops that players can choose from.
- These combinations vary in:
  - Yield
  - Time to harvest
  - Overall cost (Research Points)
- You can only apply **one fertilizer per cycle**, adding another layer of complexity.

> So, how do we find the most **efficient** harvesting plan?

Each combination of crops demands a **custom-tailored solution**, and this application provides that.

---

## 🧠 The Solution

This tool uses an **A\*** search algorithm to compute the **optimal fertilizer plan** over a set number of farming cycles (e.g., 15, dynamically changed).

It intelligently considers:
- Fertilizer durations and effects
- Crop types and their interactions with fertilizer
- Cost-efficiency (yield vs. zenny/Research Points)
- Strategic use of effects to extend other fertilizers

The result:  
A per-cycle fertilizer schedule that maximizes your return on investment.

---

## 📊 Resources

- **Crop & Fertilizer Spreadsheet**:  
  [Botanical Research Cultivation Spreadsheet](https://docs.google.com/spreadsheets/d/1weDio4wDaDbZH8zca0rB35_vDoCsdW9CwId_r8dWtFU/edit?usp=sharing)

- **In-Game Fertilizer Info**:  
  [Fertilizers in Botanical Research - Fextralife Wiki](https://monsterhunterworld.wiki.fextralife.com/Botanical+Research#Fertilizers)

---

## 🚀 Usage

To use this application:

1. Choose your desired crops (e.g., Herb, Honey, Blue Mushroom).
2. Set the number of cycles (e.g., 15).
3. Run the optimizer to compute the ideal fertilizer schedule.
4. Follow the generated plan in-game, applying one fertilizer per cycle as instructed.

---

Happy hunting, hunter! 🐉  
May your harvests be bountiful and your hunts victorious.
