from Session9C import Patient, PatientQueue

def main():
    patient1 = Patient(name="John", age=20, gender="male")
    patient2 = Patient(name="fionna", age=29, gender="female")

    queue = PatientQueue
    print("Initial queue:", vars(queue))

    queue.enqueue(patient=patient1)
    queue.enqueue(patient=patient2)
    print("Initial queue:", vars(queue))


if __name__ == "__main__":
    main()