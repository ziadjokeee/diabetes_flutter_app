import 'package:flutter/material.dart';
import 'api_service.dart';

class PredictionPage extends StatefulWidget {
  const PredictionPage({super.key});

  @override
  State<PredictionPage> createState() => _PredictionPageState();
}

class _PredictionPageState extends State<PredictionPage> {
  final inputs = List.generate(10, (_) => TextEditingController());
  double? result;

  void predict() async {
    final data = {
      "age": double.parse(inputs[0].text),
      "sex": double.parse(inputs[1].text),
      "bmi": double.parse(inputs[2].text),
      "bp": double.parse(inputs[3].text),
      "s1": double.parse(inputs[4].text),
      "s2": double.parse(inputs[5].text),
      "s3": double.parse(inputs[6].text),
      "s4": double.parse(inputs[7].text),
      "s5": double.parse(inputs[8].text),
      "s6": double.parse(inputs[9].text),
    };

    final prediction = await ApiService.predict(data);
    setState(() => result = prediction);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Diabetes Prediction")),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            ...inputs.map((c) => TextField(
              controller: c,
              keyboardType: TextInputType.number,
              decoration: const InputDecoration(labelText: "Value"),
            )),
            const SizedBox(height: 20),
            ElevatedButton(onPressed: predict, child: const Text("Predict")),
            if (result != null)
              Text("Result: ${result!.toStringAsFixed(2)}",
                style: const TextStyle(fontSize: 20)),
          ],
        ),
      ),
    );
  }
}
