
print("Grunnfarge:")
colA = int(input())
colA_B = colA%1000
colA_G = round(((colA-colA_B)%1000000)/1000)
colA_R = round(((colA-colA_B-colA_G)%1000000000)/1000000)

print("Målfarge:")
colB = int(input())
colB_B = colB%1000
colB_G = round(((colB-colB_B)%1000000)/1000)
colB_R = round(((colB-colB_B-colB_G)%1000000000)/1000000)

print("Andel målfarge:")
rationB = float(input())

R = round((1-rationB)*colA_R + rationB*colB_R)
G = round((1-rationB)*colA_G + rationB*colB_G)
B = round((1-rationB)*colA_B + rationB*colB_B)

RGB = R*1000000 + G*1000 + B
print(RGB)