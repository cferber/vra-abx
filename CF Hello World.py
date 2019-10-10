def handler(context, inputs):
    greeting = "Hello, {0} from the best friend!".format(inputs["target"])
    print(greeting)

    outputs = {
      "greeting": greeting
    }

    return outputs
