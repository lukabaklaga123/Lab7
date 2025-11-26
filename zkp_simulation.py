import random

def simulate_zkp(trials=20):
    print(f"--- Simulating ZKP with {trials} trials ---")
    
    knows_password = False 
    
    success_count = 0

    for i in range(1, trials + 1):
        path_entered = random.choice(['A', 'B'])
        
        challenge = random.choice(['A', 'B'])
        
        if knows_password:
            success = True
        else:
            if path_entered == challenge:
                success = True
            else:
                success = False

        if success:
            success_count += 1
        else:
            pass

    probability = (success_count / trials) * 100
    
    print(f"\nResults for Prover (Knows Password: {knows_password}):")
    print(f"Total Trials: {trials}")
    print(f"Successful Responses: {success_count}")
    print(f"Success Rate: {probability}%")
    
    if not knows_password:
        print("Observation: As trials increase, the success rate converges to ~50%.")

if __name__ == "__main__":
    simulate_zkp(trials=20)
    # We can also simulate_zkp(trials=1000)  to see law of large numbers in action
    
