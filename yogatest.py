img_pred = image.load_img('Dataset/Validation/Ajna/3.jpeg'), target_size = (300, 300))
img_pred = image.img_to_array(img_pred)
img_pred = np.expand_dims(img_pred, axis = 0)

rslt = model.predict(img_pred)
print (rslt)
if rslt[0][0] == 1:
    prediction = "Ajna pose"
else:
    prediction = "Some other pose"

print (prediction)