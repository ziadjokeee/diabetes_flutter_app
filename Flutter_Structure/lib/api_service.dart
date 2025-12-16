import 'package:http/http.dart' as http;
import 'dart:convert';

class ApiService {
  static const String baseUrl = "https://YOUR_API_URL/predict";

  static Future<double> predict(Map<String, double> data) async {
    final response = await http.post(
      Uri.parse(baseUrl),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode(data),
    );
    final result = jsonDecode(response.body);
    return result["prediction"];
  }
}
