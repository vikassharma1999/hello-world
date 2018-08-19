import java.util.Scanner;
class Bubblesort{
	public static void main(String args[]){
		Scanner Sc=new Scanner(System.in);
		int l;
		System.out.println("Enter The Size of the array");
		l=Sc.nextInt();
		String arr[]=new String[l];
		System.out.println("Enter The elements in the array");
		for(int i=0;i<l;i++){
			arr[i]=Sc.next();
		}
		for(int i=0;i<l-1;i++){
			for(int j=0;j<l-i-1;j++){
				if(arr[j+1].compareTo(arr[j])<0){
				String  temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;

			}}
		}
		System.out.println("Your Result is:-");
		for(int i=0;i<l;i++){
			System.out.println(arr[i]);
		}

	}
}