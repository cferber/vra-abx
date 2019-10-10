def handler(context, inputs):
    greeting = "Hello, {0} from Christian!".format(inputs["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }

    return outputs
