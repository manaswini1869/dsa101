def detect_malicious_sequence(user_actions, malicious_sequences):
    """
    Detects if any malicious sequence is a subsequence of a user's actions.

    Args:
        user_actions (list): A stream of user actions.
        malicious_sequences (list of lists): A list of predefined malicious sequences.

    Returns:
        bool: True if a malicious sequence is detected, False otherwise.
    """
    # A dictionary to track the state of each potential match
    # Key: Tuple of the malicious sequence (for hashability)
    # Value: The index of the next action we expect to see
    potential_matches = {}

    for action in user_actions:
        # Create a new dictionary to hold the state for the next step
        new_potential_matches = {}

        # Check if the current action can start any new malicious sequences
        for seq in malicious_sequences:
            if seq[0] == action:
                # We've matched the first element, so the next is at index 1
                new_potential_matches[tuple(seq)] = 1
        print(action, potential_matches)
        # Iterate over our current potential matches to advance them
        for seq, next_idx in potential_matches.items():
            # Check if the current action is the one we're looking for next
            if next_idx < len(seq) and seq[next_idx] == action:
                # If we've found the next action, check if the sequence is complete
                if next_idx + 1 == len(seq):
                    return True  # Found a complete malicious sequence!

                # Otherwise, add it to our new set of potential matches
                new_potential_matches[seq] = next_idx + 1
            else:
                # If the current action doesn't advance the sequence,
                # we keep it active in case a later action matches
                new_potential_matches[seq] = next_idx

        # Update our master list of potential matches
        potential_matches = new_potential_matches

    return False

# Example Usage
user_stream = ["login", "page_view", "access_file", "view_secret_doc", "logout", "another_action"]
malicious_patterns = [["login", "view_secret_doc", "logout"]]

if detect_malicious_sequence(user_stream, malicious_patterns):
    print("Malicious sequence detected!")
else:
    print("No malicious sequence found.")