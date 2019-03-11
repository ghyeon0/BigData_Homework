#include <stdio.h>

int freq[128];  // 아스키 문자 빈도조사
int hfreq[25][94]; // 한글 빈도조사

main()
{
	int ch, i, j, c1, c2;

	while ((c1 = getchar()) != EOF) {
		if (c1 & 0x80) c2 = getchar();

		if (c1 < 128) freq[c1]++; // ASCII 문자 빈도조사

		if (c1 >= 0xB0 && c1 <= 0xC8 &&
		    c2 >= 0xA1 && c2 <= 0xFE) // 한글 빈도조사
		hfreq[c1-0xB0][c2-0xA1]++;
	}

	for (i = 0; i < 128; i++) {
		if (freq[i]) // ASCII 문자 빈도조사
			printf("\tf[%c] = %d", i, freq[i]);
	}

	putchar('\n');

	for (i=0xB0; i <= 0xC8; i++) { // 한글 빈도조사
		for (j=0xA1; j <= 0xFE; j++) {
			if (hfreq[i-0xB0][j-0xA1])
				printf("\tf[%c%c] = %d", i, j, hfreq[i-0xB0][j-0xA1]);
		}
	}
}
