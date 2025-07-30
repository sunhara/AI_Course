import pygame
import sys
from constrain import*
from gameplay import*
from aprior import*


def main():
    game = Casher()
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            

            # Handle events
            if event.type == pygame.QUIT:
                # Quit the game if the window is closed
                pygame.quit()
                sys.exit()
                
            # all the mouse click events
            if item_button1.is_clickedLeft(event):
                game.item1 = game.item1+1
            if game.item1>0 and item_button1.is_clickedRight(event):
                game.item1 = game.item1-1
                
            if item_button2.is_clickedLeft(event):
                game.item2 = game.item2+1
            if game.item2>0 and item_button2.is_clickedRight(event):
                game.item2 = game.item2-1              
 
            if item_button3.is_clickedLeft(event):
                game.item3 = game.item3+1
            if game.item3>0 and item_button3.is_clickedRight(event):
                game.item3 = game.item3-1    
                
            if item_button4.is_clickedLeft(event):
                game.item4 = game.item4+1
            if game.item4>0 and item_button4.is_clickedRight(event):
                game.item4 = game.item4-1    
           
            if item_button5.is_clickedLeft(event):
                game.item5 = game.item5+1
            if game.item5>0 and item_button5.is_clickedRight(event):
                game.item5 = game.item5-1
            
            if item_button6.is_clickedLeft(event):
                game.item6 = game.item6+1
            if game.item6>0 and item_button6.is_clickedRight(event):
                game.item6 = game.item6-1
            
            if item_button7.is_clickedLeft(event):
                game.item7 = game.item7+1
            if game.item7>0 and item_button7.is_clickedRight(event):
                game.item7 = game.item7-1
            
            if item_button8.is_clickedLeft(event):
                game.item8 = game.item8+1
            if game.item8>0 and item_button8.is_clickedRight(event):
                game.item8 = game.item8-1
            
            if item_button9.is_clickedLeft(event):
                game.item9 = game.item9+1
            if game.item9>0 and item_button9.is_clickedRight(event):
                game.item9 = game.item9-1
            
            if item_button10.is_clickedLeft(event):
                game.item10 = game.item10+1
            if game.item10>0 and item_button10.is_clickedRight(event):
                game.item10 = game.item10-1           
            
            if trans_button.is_clickedLeft(event):
                game.transaction()
                
                screen.fill((WHITE))
                text_surface_cleared = font.render("TRANSACTION!!!", True, GREEN)
                screen.blit(text_surface_cleared,(250,250))
                pygame.display.flip()
                pygame.time.delay(1000)

##############################################################
            if kmeans_button.is_clickedLeft(event):
                game.kmeans()
                
                
                screen.fill((WHITE))
                text_buyer1 = font.render("RED is Traget Buyers", True, RED)
                text_buyer2 = font.render("BLUE is Non-Target Buyers/Broad Market", True, BLUE)
                screen.blit(text_buyer1,(250,250))
                screen.blit(text_buyer2,(250,350))
                pygame.display.flip()
                pygame.time.delay(2000)
                
            if associ_button.is_clickedLeft(event):
                
                file = open("data.txt", "r")
                transactions_names = []

                for line in file:
                    subtransactions=[]
                    # Remove trailing comma and split by comma
                    items = line.split(",")
                    for item in items:
                        if ':' in item:
                            
                            item_parts = item.split(':')
                            item_name = item_parts[0]
                            
                            subtransactions.append(item_name)
                            transactions_names.append(subtransactions)
        
                apriori_alg = AprioriAlgorithm(min_support=0.3, min_confidence=0.6)
                
                # Load transactions
                apriori_alg.load_transactions(transactions_names)
                
                # Find frequent itemsets
                frequent_itemsets = apriori_alg.find_frequent_itemsets()
                
                # Generate association rules
                association_rules = apriori_alg.generate_association_rules()

                # Extract all unique item names
                data = association_rules

                itemsets = set()
                for rule in data:
                    # Combine antecedent and consequent to get full itemset
                    full_itemset = rule['antecedent'].union(rule['consequent'])
                    itemsets.add(frozenset(full_itemset))
                
                # Sort itemsets by size and then alphabetically
                sorted_itemsets = sorted(itemsets, key=lambda x: (len(x), sorted(list(x))))
                
                # Build the output as a multiline text variable
                output_lines = []
                output_lines.append("ITEM COMBINATIONS:")
                output_lines.append("=" * 30)
                
                for i, itemset in enumerate(sorted_itemsets, 1):
                    items = sorted(list(itemset))
                    output_lines.append(f"{i:2d}. {', '.join(items)}")
  
                # Create the multiline text variable
                item_combinations_text = "\n".join(output_lines)
                
                

                result1 = apriori_alg.print_frequent_itemsets()
                result2 = apriori_alg.print_association_rules()
                print(result1)
                print(result2)
                
                result = item_combinations_text
                
                screen.fill((WHITE))
                
                lines = result.splitlines()
        
                y = 10
                counter = 0
                line_height = 25
                k = 20
                for line in lines:
                    if counter < k:
                
                        text_surface = tinyfont.render(line, True, RED)
                        screen.blit(text_surface, (10, y))
                        y += line_height  # Move to next line position
                        counter += 1
                    else:
                        
                        text_surface = tinyfont.render(line, True, RED)
                        screen.blit(text_surface, (500, y-((k-1)*25)))
                        y += line_height  # Move to next line position
                        counter += 1

                    pygame.display.flip()
                    
                    
                pygame.time.delay(3000)
                    

                
            if rand_trans_button.is_clickedLeft(event):
                game.generateTrans()
                
                screen.fill((WHITE))
                text_surface_cleared = font.render("5 Random TRANSACTIONS", True, GREEN)
                screen.blit(text_surface_cleared,(250,250))
                pygame.display.flip()
                pygame.time.delay(1000)  
            
              
            if reset_button.is_clickedLeft(event):
                game.reset()
            
            if clear_button.is_clickedLeft(event):
                game.clear()
                
                screen.fill((WHITE))
                text_surface_cleared = font.render("DATA CLEARED!!!", True, RED)
                screen.blit(text_surface_cleared,(250,250))
                pygame.display.flip()
                pygame.time.delay(1000)


                

    # Draw everything
    
        game.draw_ui()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()