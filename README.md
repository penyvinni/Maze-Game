# Maze-Game
An interesting problem is the design of labyrinths. In this paper we are asked to create labyrinths using the structure of disjoint sets. Then we are asked to draw the path from the entrance to the exit of the labyrinth using the Breadth First Search algorithm.


# Περιγραφή της Υλοποίησης
Το πρόβλημα του λαβύρινθου είναι ένα πρόβλημα στο οποίο δίνεται μήκος, ύψος, είσοδο και έξοδος (θετικές ακέραιες τιμές) και ζητείται να βρεθεί μια σειρά από ακμές που θα οδηγει από την είσοδο στην έξοδο με τον πιο συντομότερο τρόπο. Για τη σχεδίαση του χρησιμοποιήθηκε δομή Union - Find και τα disjoint sets όπου στις ήδη αφαιρεμένες κορυφές βρίσκει τις κορυφές εκείνες που δεν έχουν επισκεφτεί και τις προσθέτει στις removed edges, ενώνοντας τες όλες μάζι για να δημιουργηθεί ένα μονοπάτι. Το μόνο απαραίτητο όμως είναι να ανήκει η είσοδος και η έξοδος στο ίδιο σύνολο.

# Αποτελέσματα
Για την συγγραφή της εργασίας χρησιμοποιήθηκε η Python 3.9.2 και το Visual Studio Code.
Τα χαρακτηριστικά του υπολογιστή είναι Intel Core i7-1065G7 (1.30GHz - 1.50 GHz), 8 GB DDR3 (2667 MHz), λειτουργικό σύστημα Windows 10 Home x64. Για την οπτικοποίηση των αποτελεσμάτων χρησιμοποιήθηκε η βιβλιοθήκη matplotlib. Στον πίνακα φαίνονται τα αποτελέσματα του κώδικα για τον λαβύρινθο 3x3 και στην εικόνα 2.1 φαίνεται η δημιουργία του λαβύρινθου 3x3 με την εκτέλεση του κώδικα. 
Τέλος, οδηγίες για την εκτέλση του κώδικα: python maze.py

![table)](https://github.com/user-attachments/assets/0eb1cfe5-8654-4b99-a91f-8c20845e9f58)
![maze](https://github.com/user-attachments/assets/6e2ea4f2-c6a7-4d0c-b4b1-d79513b83816)
