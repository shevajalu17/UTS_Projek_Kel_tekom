def validate_variable_name(input_str: str) -> tuple[bool, list[str]]:
    current_state = 'q0'
    accept_states = {'q1'}
    trace = [f"Start at {current_state}"]
    
    for char in input_str:
        if current_state == 'q0':
            if char.isalpha() or char == '_':
                current_state = 'q1'
            else:
                current_state = 'q_dead'
                
        elif current_state == 'q1':
            if char.isalnum() or char == '_':
                current_state = 'q1'
            else:
                current_state = 'q_dead'
                
        elif current_state == 'q_dead':
            current_state = 'q_dead'
            
        trace.append(f"Input '{char}' -> Move to {current_state}")
    
    is_valid = current_state in accept_states
    return is_valid, trace

if __name__ == "__main__":
    print("=== TEST CASE DFA VALIDASI VARIABLE NAME ===")
    test_inputs = ["nama_user", "_count1", "123name", "user-name"]

    for test in test_inputs:
        valid, trace = validate_variable_name(test)
        status = "VALID (ACCEPT)" if valid else "TIDAK VALID (REJECT)"
        print(f"\nInput: '{test}' => {status}")
        print("Trace:", " -> ".join(trace))