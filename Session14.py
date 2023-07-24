"""
    We need to create an application for vets
    1. Vet should be able to add a customer
    2. Vet should be able to add pets of customer
    3. Vet should be able to add a consultation with medicines/prescription for customer's pet

   Principle of OOPS
    1. Identify Objects
        customer : name, phone, email, age, address, gender, createdon
        pet : name, age, breed, weight, gender, createdon
        consultation : customer, pet, problem, heartrate, temperature, medicines, createdon

        Identify relations
        1 customer can have many pets
        1 customer can have many consultations for many pets

    2. Write class
    3. You create real object from Classes

   DB Connectivity
    4. Whatever object has been created should be saved in memory

"""



