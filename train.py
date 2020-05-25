from dataset import GetDataset
from model import GetModel


epochs = 60
input_shape = (64, 64, 3)
num_classes = 4
batch_size = 128


(train, val) = GetDataset(batch_size)
model = GetModel(input_shape, num_classes)


train_steps = train.n / train.batch_size
val_steps = val.n / val.batch_size


model.compile(optimizer='adam',
              loss='categorical_crossentropy', metrics=['acc'])


history = model.fit_generator(generator=train,
                              steps_per_epoch=train_steps,
                              validation_data=val,
                              validation_steps=val_steps,
                              epochs=epochs,
                              verbose=1)


model.save('my_model.h5')
