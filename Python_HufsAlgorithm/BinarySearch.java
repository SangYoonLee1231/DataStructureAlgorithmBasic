// 자바 학부 수업에 다룬 - 이진 트리(Binary Search) 검색 알고리즘

import java.util.Arrays;

// 클래스로 구현
class BinarySearch
{
	int binarySearch(int[] list, int key)
	{
		int low = 0;
		int high = list.length - 1;
		
		while(low <= high)
		{
			int middle = (int) ((high + low) / 2);
			
			if (key < list[middle]) {
				high = middle - 1;
			}
			else if (key == list[middle]) {
				return middle;
			}
			else {
				low = middle + 1;
			}
			
		}
		return -1;
	}
}

public class BinarySearchEx {
	
	// 함수+재귀호출로 구현
	public static int binarySearch(int[] a, int start, int end, int key) {
		int middle = (int) ((start + end) / 2);
		
		if (key == a[middle])
			return 1;
		else if (key <= a[middle])
			return binarySearch(a, start, middle-1, key);
		else if (key >= a[middle])
			return binarySearch(a, middle+1, end, key);
		else
			return -1;
	}
	
	
	public static void main(String[] args) {
		int a[] = {1, 3, 5, 6, 7, 9, 11, 15, 19, 30};
		int key = 15;
		
		int isExist = binarySearch(a, 0, a.length - 1, key);
		System.out.println(isExist);
		
		
		BinarySearch bs = new BinarySearch();
		
		System.out.println(bs.binarySearch(a, key));
		System.out.println(bs.binarySearch(a, 17));
		System.out.println(bs.binarySearch(a, 3));
		
		// 내부 메소드 이용 (Array 클래스 import)
		System.out.println(Arrays.binarySearch(a, key));
		System.out.println(Arrays.binarySearch(a, 17));
		System.out.println(Arrays.binarySearch(a, 3));
	}

}
