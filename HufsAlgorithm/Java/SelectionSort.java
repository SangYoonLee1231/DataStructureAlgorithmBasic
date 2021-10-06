// 자바 - Selection Sort (선택 정렬) 알고리즘

import java.util.Arrays;

class SelectionSort
{
	void SelectionSort(int[] list)
	{
		int temp = 0;
		
		for (int i = 0; i < list.length; i++)
		{	
			int min = list[i];
			int min_index = -1;

			for (int j = i; j < list.length; j++) {
				if (min >= list[j]) {
					min = list[j];
					min_index = j;
				}
			}

			temp = list[i];	//list[맨앞자리] <--> minimum값
			list[i] = list[min_index];
			list[min_index] = temp;
		}
	}
}

public class SelectionSortEx
{

	public static void main(String[] args)
	{
		int[] list = {69, 10, 30, 2, 19, 8, 31, 22};
		
		System.out.print("Original List : ");
		for (int i = 0; i < list.length; i++)
			System.out.print(list[i] + " ");
		System.out.println();
		
		// 클래스로 구현
		SelectionSort ss = new SelectionSort();
		ss.SelectionSort(list);
		
		// 내장 함수 이용
		//Arrays.sort(list);
		
		System.out.print("Sorted List : ");
		for (int i = 0; i < list.length; i++)
			System.out.print(list[i] + " ");	
	}
}
