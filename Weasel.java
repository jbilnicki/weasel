//package com.test.service;
import java.util.concurrent.TimeUnit;
import java.util.Scanner;
import java.util.Random;
//import java.util.LinkedList;
import java.util.ArrayList;
//import java.util.Charset;
public class Weasel {
	public static void main(String[] args){
		System.out.println("Do jakiego słowa ma dążyć program?");
		System.out.println("Nie używaj polskich znaków ani spacji! ");
		// pobranie danych od użytkownika
		Scanner scanner = new Scanner(System.in);
		String word = scanner.next();
		System.out.println("---------------------------------------------------");
		
		int len = word.length();
		byte[] array = new byte[len];
		Random generator = new Random();
		generator.nextBytes(array);
		//String generatedString = new String(array, Charset.forName("UTF-8"));
		String generatedString = new String(array);
		double mutationP = 0.3;
		
		System.out.println(generatedString);
		//System.out.println("długość ciągu znaków: " + len);
		
		//double mutation = generator.nextDouble();
		//System.out.println("mutacja " + mutation);
		//byte[] b = new byte[1];
		//char wordPart = generator.nextBytes(b);
		//char wordPart = (char)(generator.nextInt(26) + 'a');
		//System.out.println("losowy znak " + wordPart);
		
		boolean check = word.equals(generatedString);
		//System.out.println(check);
		
		/*String w = "dupka";
		boolean check2 = word.equals(w);
		System.out.println(check2);*/
		
		while (check == false) {
			//LinkedList offspring = new LinkedList();
			ArrayList <String> offspring = new ArrayList <>();

			for (int i = 0; i<50; i++) {
				// mutowanie sekwencji
				String child = new String();
				for (char wordPart : generatedString.toCharArray()) {
					double mutation = generator.nextDouble();
					if (mutation < mutationP) {
						wordPart = (char)(generator.nextInt(26) + 'a');
					}
					child += wordPart;
				}
				offspring.add(child);
			}
			//System.out.println("Potomstwo: " + offspring);
			
			
			ArrayList <Integer> similarities = new ArrayList <Integer>();
			//LinkedList similarities = new LinkedList();
			
			// test zamiany wartości stringów
			//String a = "apple";
			//String b = "pear";
			//a = b;
			//System.out.println(a + b);
			/*String dupa = "dupa";
			String kupa = "kupa";
			if (dupa.charAt(1) == kupa.charAt(1)) {
				System.out.println("prawda");
			} else {
				System.out.println("fałsz");
			}*/
			
			//System.out.print("test Stringa: " + word.charAt(1));
			
			/*for (String child : offspring) {
				int similarity = 0;
				for (int i = 0; i < len; i++){
					// porównanie odpowiadających sobie znaków
					if (child.charAt(i) == word.charAt(i)) {
						similarity++;
					}
				}
				similarities.add(similarity);
			}
			System.out.println(similarities);*/
			
			//int len2 = offspring.size();
			for (int j = 0; j < offspring.size(); j++) {
				int similarity = 0;
				String child = offspring.get(j);
				for (int i = 0; i < len; i++){
					// porównanie odpowiadających sobie znaków
					if (child.charAt(i) == word.charAt(i)) {
						similarity++;
					}
				}
				similarities.add(similarity);
			}
			//System.out.println(similarities);
			String mostSimilar = new String();
			int largest = 0;
			for (int i = 0; i < similarities.size(); i++) {
				if (largest <= similarities.get(i)) {
					largest = similarities.get(i);
					mostSimilar = offspring.get(i);
				}
			}
			//System.out.println("Najwiekszy: " + largest);
			//System.out.println("Najbardziej podobny: " + mostSimilar);
			generatedString	= mostSimilar;
			//System.out.println("Nowa sekwencja rodzicielska: " + generatedString);
			System.out.println(generatedString);
			check = word.equals(generatedString);
			// zatrzymuje kod na 1 sekundę
			//Weasel.sleep(1000);
			try {
				TimeUnit.SECONDS.sleep(1);
			} catch (InterruptedException ie) {
				Thread.currentThread().interrupt();
			}
			/*try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }*/
			//System.out.println("kocham moją mięsinkę");
		}
	}
}
